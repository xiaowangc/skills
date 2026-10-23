#!/usr/bin/env python3
"""Read-only Git evidence collector; the skill generates the narrative report."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import subprocess
from datetime import date, datetime, time, timedelta
from zoneinfo import ZoneInfo


def git(repo, *args, stdin=None):
    result = subprocess.run(
        ['git', '-C', str(repo), '--no-pager', *args], input=stdin,
        stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=120,
        env=dict(os.environ, GIT_OPTIONAL_LOCKS='0', GIT_TERMINAL_PROMPT='0'))
    if result.returncode:
        raise RuntimeError(f'git {args[0]} failed (exit {result.returncode})')
    return result.stdout


def period(now, timezone, end_date=None):
    zone = ZoneInfo(timezone)
    now = now.astimezone(zone)
    friday = date.fromisoformat(end_date) if end_date else now.date() - timedelta(days=(now.weekday()-4) % 7)
    if friday.weekday() != 4:
        raise ValueError('--end-date must be a Friday')
    end = datetime.combine(friday, time(17), zone)
    if not end_date and end > now:
        end -= timedelta(days=7)
    if end > now:
        raise ValueError('Reporting cutoff has not been reached')
    return end - timedelta(days=7), end


def collect_repo(path, emails, start, end):
    repo = Path(path).resolve()
    if not repo.is_dir():
        raise RuntimeError('Repository directory missing')
    git(repo, 'rev-parse', '--git-dir')
    shallow = git(repo, 'rev-parse', '--is-shallow-repository').strip() == b'true'
    refs = git(repo, 'for-each-ref', '--format=%(refname)', 'refs/heads', 'refs/remotes').decode().splitlines()
    has_head = subprocess.run(['git', '-C', str(repo), 'rev-parse', '--verify', 'HEAD'],
                             stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=30).returncode == 0
    revisions = (['HEAD'] if has_head else []) + refs
    # Continue through old-dated ancestors: commit times need not be monotonic.
    raw = git(repo, 'log', *revisions, f'--since-as-filter={start.isoformat()}',
              '--format=%H%x00%aI%x00%cI%x00%ae%x00%an%x00%P%x00%s%x00') if revisions else b''
    fields = raw.decode('utf-8', errors='replace').split('\x00')
    records = []
    for offset in range(0, len(fields)-1, 7):
        sha, authored, committed, email, author, parents, subject = fields[offset:offset+7]
        sha = sha.strip()
        modified = datetime.fromisoformat(committed)
        if email.casefold() not in emails or not (start <= modified < end):
            continue
        merge = len(parents.split()) > 1
        files = [] if merge else [p.decode('utf-8', errors='replace') for p in git(
            repo, 'diff-tree', '--root', '--no-commit-id', '--name-only', '-r', '-z', sha).split(b'\x00') if p]
        patch_id = None
        if not merge:
            patch = git(repo, 'show', '--format=', '--no-ext-diff', '--no-textconv', '--binary', '--full-index', sha)
            hashed = git(repo, 'patch-id', '--stable', stdin=patch).split()
            patch_id = hashed[0].decode() if hashed else None
        branches = git(repo, 'for-each-ref', f'--contains={sha}', '--format=%(refname:short)',
                       'refs/heads', 'refs/remotes').decode().splitlines()
        records.append({'sha': sha, 'subject': subject, 'author': author, 'author_email': email,
                        'author_time': datetime.fromisoformat(authored).astimezone(end.tzinfo).isoformat(),
                        'modified_time': modified.astimezone(end.tzinfo).isoformat(),
                        'is_merge': merge, 'branches': branches, 'files': files,
                        'module_hints': sorted({p.split('/')[0] if '/' in p else '(repository root)' for p in files}),
                        'patch_id': patch_id})
    records.sort(key=lambda r: (r['modified_time'], r['sha']))
    patches = {}
    for record in records:
        if record['patch_id']:
            patches.setdefault(record['patch_id'], []).append(record['sha'])
    return {'service': repo.name, 'repository': str(repo), 'status': 'ok', 'shallow': shallow,
            'commits': records, 'duplicate_patch_candidates': [v for v in patches.values() if len(v) > 1]}


def save_evidence(path, payload):
    content = json.dumps(payload, ensure_ascii=False, indent=2)+'\n'
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists():
        old = path.read_text()
        if old == content:
            return
        backup = path.parent / '_备份' / f'{path.stem}_{hashlib.sha256(old.encode()).hexdigest()[:16]}.json'
        backup.parent.mkdir(exist_ok=True)
        if not backup.exists():
            backup.write_text(old)
    temporary = path.with_suffix('.tmp')
    temporary.write_text(content)
    temporary.replace(path)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--config', type=Path, default=Path(__file__).resolve().parents[1] / 'references/config.json')
    parser.add_argument('--end-date', help='Reporting Friday, YYYY-MM-DD; default: latest completed cutoff')
    args = parser.parse_args()
    if not args.config.is_file():
        parser.error('Configuration missing: copy references/config.example.json to references/config.json, fill in your workspace settings, or pass --config /absolute/path/to/config.json')
    cfg = json.loads(args.config.read_text())
    start, end = period(datetime.now(ZoneInfo(cfg['timezone'])), cfg['timezone'], args.end_date)
    emails = {s.casefold() for s in cfg['author_emails']}
    if not emails or not cfg['repositories']:
        raise ValueError('Author email and repository list must not be empty')
    results = []
    for path in dict.fromkeys(str(Path(p).resolve()) for p in cfg['repositories']):
        try:
            results.append(collect_repo(path, emails, start, end))
        except (RuntimeError, subprocess.TimeoutExpired, OSError, ValueError) as exc:
            results.append({'service': Path(path).name, 'repository': path, 'status': 'error',
                            'error': str(exc), 'commits': []})
    succeeded = sum(r['status'] == 'ok' for r in results)
    commits = [c for r in results for c in r['commits']]
    payload = {'schema_version': 1, 'timezone': cfg['timezone'], 'start_inclusive': start.isoformat(),
               'end_exclusive': end.isoformat(), 'author_emails': sorted(emails),
               'time_basis': 'committer_time', 'coverage': 'HEAD + local + cached remote branches; no fetch',
               'repositories': results, 'summary': {'repositories_total': len(results),
               'repositories_ok': succeeded, 'repositories_failed': len(results)-succeeded,
               'active_repositories': sum(bool(r['commits']) for r in results),
               'non_merge_commits': sum(not c['is_merge'] for c in commits),
               'merge_commits': sum(c['is_merge'] for c in commits)}}
    stamp = end.strftime('%Y%m%d')
    output = Path(cfg['output_directory']) / '_数据' / f'{stamp}_git.json'
    save_evidence(output, payload)
    print(json.dumps({'evidence': str(output), 'report': str(output.parent.parent / f'{stamp}_周报.md'),
                      'summary': payload['summary']}, ensure_ascii=False))
    return 2 if not succeeded else (1 if succeeded < len(results) else 0)


if __name__ == '__main__':
    raise SystemExit(main())
