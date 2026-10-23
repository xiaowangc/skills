## What it does

`git-weekly-report` turns your local Git commits into a personal weekly report, grouped by service and module with modification times and commit evidence. It attributes work by author email and uses committer time to place each change in the reporting period.

The report describes committed work. Merges are recorded separately, and commits alone do not establish that a feature was deployed or accepted.

## When to reach for it

Type `/git-weekly-report`, or let it be selected automatically when you ask for a personal report from local Git history. A scheduled task can explicitly invoke it with the same configuration.

| Request | Reporting period |
| --- | --- |
| Generate a weekly report | The most recent completed Friday cutoff, covering the preceding seven days |
| Backfill a report | The explicitly requested Friday cutoff |

## Prerequisites

Python 3.9 or later, Git, and local repositories are required. Configure author emails, absolute repository paths, the output directory and timezone in a private configuration file. The distributed example contains no personal workspace settings.

## Evidence before summary

The report links each outcome back to commits and names the service, module and modification time. Local and cached remote branches are included without fetching. Identical commits are counted once, and matching patch IDs identify candidates for repeated patches such as cherry-picks.

Missing repositories and stale cached history remain visible in the coverage notes. The collector saves structured evidence beside the report, so an empty period can be distinguished from a failed collection.

## Common questions

**Why is the report empty when I have recent work?**

Check the reporting cutoff, configured author emails and local branch data. Uncommitted changes and remote commits that have not been fetched are outside the report's evidence. The skill does not fetch automatically.

**Does installing the skill activate the Friday schedule?**

No. Configure a separate scheduled task to invoke it every Friday at 17:00 in the chosen timezone. The skill also supports manual runs and historical backfills.

## It's working if

- Every outcome names a service and module, with a modification time and traceable commits.
- Merge operations do not inflate the implementation summary.
- Missing data is identified rather than presented as an empty work week.
- Regenerating a report preserves manual additions and backs up changed evidence.

## Where it fits

`git-weekly-report` is a standalone reporting tool for manual use or a recurring schedule. It summarises local Git evidence rather than passing a live conversation to another person or tool. [ask-matt](https://aihero.dev/skills-ask-matt) maps it alongside the other standalone workflows.
