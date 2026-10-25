## What it does

`dingtalk-docs` creates, reads, edits, restructures, formats, imports, exports, and manages DingTalk online documents through the official document MCP. It treats the MCP as the primary document surface, so an agent can work from stable document and block identifiers instead of fragile browser clicks.

The skill chooses the smallest write that achieves the result. A section edit stays a section edit; a full overwrite is reserved for work that genuinely needs a full rebuild and is protected by a version checkpoint.

## When to reach for it

Type `/dingtalk-docs`, or the agent reaches for it automatically when a request involves an `alidocs.dingtalk.com` document, DingTalk knowledge base, or DingTalk document publishing workflow.

Use [document co-authoring](https://aihero.dev/skills-doc-coauthoring) first when the argument or content is still unsettled. Use a Word document tool when the target is a local `.docx` rather than a DingTalk online document.

## Prerequisites

The official DingTalk document MCP must be connected and authorized. OAuth is preferred where the client supports it. Instance URLs containing a `key` are credentials and belong in the client's secret-backed MCP configuration, never in a repository.

## Smallest write

The leading idea is **smallest write**. The skill reads the current state, identifies the narrowest mutation surface, writes there, and verifies with a fresh read.

| Situation | Write surface |
| --- | --- |
| New document | Markdown at creation time |
| Additional section | Append at the document boundary |
| Existing section or heading | Block-level update |
| Complete structural rewrite | Version checkpoint, then explicit overwrite |
| Cover or background | Document style update |

This keeps comments, attachments, images, and concurrent edits outside the blast radius whenever possible.

## Common questions

**Can it improve the layout of an existing document?**

Yes. It reads the existing Markdown and blocks, then improves heading hierarchy, paragraph length, lists, tables, callouts, code blocks, cover, or background. Content changes beyond the requested scope remain out of bounds.

**Why not just automate the browser?**

The MCP exposes document, block, style, version, import, export, and permission operations directly. Browser automation is less stable and is kept for capabilities the MCP does not expose.

**Will it overwrite my document?**

Not by default. The skill always passes the update mode explicitly, prefers block updates or append, and protects a necessary overwrite with a current read and version checkpoint.

## It's working if

- The trace resolves the exact document from its URL or returned identifier, without guessed IDs.
- A small edit changes only the intended block or section.
- A structural rewrite has a recoverable version and a post-write verification read.
- MCP credentials never appear in source files or the final response.
- Permissions and collaborator notifications remain unchanged unless explicitly requested.

## Where it fits

`dingtalk-docs` is a reach-for-it-anytime standalone for publishing and maintaining DingTalk documents. It commonly follows [document co-authoring](https://aihero.dev/skills-doc-coauthoring), which settles the content, while this skill performs the platform-specific write. See [ask-matt](https://aihero.dev/skills-ask-matt) for the map of the full skill set.
