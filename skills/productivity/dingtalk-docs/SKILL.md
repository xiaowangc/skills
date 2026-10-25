---
name: dingtalk-docs
description: Create, read, edit, restructure, format, import, export, or manage DingTalk online documents and knowledge-base nodes through the official DingTalk document MCP. Use for alidocs.dingtalk.com links and requests to write or improve DingTalk docs. Use a DOCX-specific skill for local Word files.
---

# DingTalk documents

Use the official DingTalk document MCP as the source of truth and mutation surface. A DingTalk URL is a target identifier, not permission to alter unrelated nodes or sharing settings.

## Route the request

1. Discover the available DingTalk document MCP tools before using browser automation or scraping.
2. Resolve the narrowest target:
   - For an exact `alidocs.dingtalk.com` URL or node ID, call `get_document_info` and operate on that node.
   - For a selected knowledge base or folder, traverse with `list_nodes`.
   - Use `search_documents` only when the user has not supplied a narrower scope.
3. Read current state before editing. Use `get_document_content`; add `list_document_blocks` for partial or layout-sensitive edits, and `get_document_style` when cover or background matters.
4. Make the smallest mutation that satisfies the request, then read the affected content or metadata again and verify the observable result.

If the MCP is unavailable, read [MCP setup](references/mcp-setup.md). Browser editing is a last resort for a capability the MCP does not expose, not an authentication workaround.

## Write with structure

Treat Markdown as the portable layout layer. Preserve the author's meaning while improving hierarchy with headings, short paragraphs, lists, tables, blockquotes, callouts, and fenced code blocks. Use real newline characters in MCP Markdown arguments.

Choose the write path by blast radius:

| Need | Preferred operation |
| --- | --- |
| Create a text document | `create_document`, with initial Markdown when it fits |
| Add material without disturbing existing content | `update_document` with `mode: append` |
| Change one section or block | `list_document_blocks`, then block insert or update tools |
| Rebuild the full structure | Save a version, then `update_document` with an explicit `mode: overwrite` |
| Change cover or background | `update_document_style` |
| Start from an organisation template | `list_doc_templates` or `search_doc_templates`, then `apply_doc_template` |

For substantial content whose purpose or argument is unsettled, use `doc-coauthoring` to develop the text first, then publish it through this skill.

## Guardrails

- Extract every `nodeId`, `blockId`, folder ID, workspace ID, revision, and template ID from the user or a tool response. Never invent identifiers.
- Treat an MCP URL containing `key` and every OAuth token as a secret. Keep it out of skill files, repositories, examples, logs, and final responses.
- `update_document` defaults to overwrite. Always pass `mode` explicitly.
- Before overwrite, read the current document, inspect for rich blocks that Markdown may not preserve, and call `save_doc_version` when available. Ask before overwrite if it can remove images, attachments, comments, or unsupported blocks.
- Prefer the current revision when the update tool accepts one. If it changed since the read, re-read and reconcile instead of forcing the write.
- Confirm immediately before deleting nodes or blocks, transferring ownership, removing permissions, or replacing a file. These are separate authorities from ordinary document editing.
- Do not change permissions or notify collaborators unless the user asked for that outcome.
- Respect tool limits. `create_document` and each `update_document` write accept at most 10,000 characters in the current MCP. Split longer content at block boundaries and verify ordering.

For the current v1 tool families and format limits, read [MCP v1 capabilities](references/mcp-v1.md) only when the task needs those branches.

## Completion

Finish only when the requested document state is visible through a fresh MCP read. Report the document title or URL, the kind of mutation made, any content the chosen format could not preserve, and whether permissions or sharing remained unchanged.
