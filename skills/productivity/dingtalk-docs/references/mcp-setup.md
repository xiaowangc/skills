# DingTalk document MCP setup

Use the official OAuth resource endpoint when the client supports remote MCP authorization:

`https://mcp-gw.dingtalk.com/oauth/server/doc`

The endpoint advertises OAuth protected-resource metadata and an authorization-code flow with PKCE. Let the MCP client open the authorization page and store the resulting credential in its secret store.

An administrator may instead provide an instance URL shaped like:

`https://mcp-gw.dingtalk.com/server/<instance-id>?key=<secret>`

Treat the complete URL as a credential. Configure it in the MCP client's secret-backed settings. Never paste a real instance URL into source files, skill content, examples, issue comments, or command output.

After setup, discover tools from the connected server. The marketplace instance evolves independently of this skill, so the live schema wins over cached names in the reference.

Official entry points:

- DingTalk document platform overview: https://open.dingtalk.com/document/development/dingtalk-document-overview
- DingTalk document MCP marketplace: https://aihub.dingtalk.com/#/mcp-market/detail?mcpId=9629
