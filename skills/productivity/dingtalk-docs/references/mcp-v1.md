# DingTalk document MCP v1 capabilities

This is a routing reference, not a replacement for live tool discovery.

## Content and layout

- `create_document`, `get_document_content`, `update_document`
- `list_document_blocks`, `insert_document_block`, `update_document_block`, `delete_document_block`
- `get_document_style`, `update_document_style`
- `list_doc_versions`, `save_doc_version`, `revert_doc_version`

Only DingTalk text documents (`adoc`) support Markdown content operations. Current create and update calls accept at most 10,000 characters per write. Markdown strings require real newlines. Block APIs currently address top-level blocks; use returned `blockId` values.

## Discovery and organisation

- `get_document_info`, `search_documents`, `get_recent_list`
- `list_nodes`, `create_folder`, `move_document`, `copy_document`, `rename_document`, `delete_document`
- `list_doc_templates`, `search_doc_templates`, `apply_doc_template`

Folder and workspace parameters select the destination. A specific folder takes precedence over a workspace root when both are accepted.

## Transfer and files

- Import: `create_import_session`, upload to the returned URL, `confirm_import`, then `query_import_task`
- Export: `submit_export_job`, then `query_export_job`
- File upload: `get_file_upload_info`, upload bytes, then `commit_uploaded_file`
- Attachments: `get_doc_attachment_upload_info`, upload bytes, then reference the resulting resource; use `download_doc_attachment` to fetch one
- File download: `download_file`

## Permissions

- `list_permission`, `add_permission`, `update_permission`, `remove_permission`
- `transfer_owner`

Permission mutations are not implied by permission to edit content. Obtain explicit user intent for the specific sharing or ownership change.
