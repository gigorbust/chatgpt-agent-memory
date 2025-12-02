# Uninstall Atlassian Software

- [/] Identify installed Atlassian software <!-- id: 0 -->
    - Found `mcp-remote` processes connecting to `atlassian.com`

- [x] Stop running Atlassian processes <!-- id: 1 -->
- [x] Remove Application files <!-- id: 2 -->
    - No standard applications found
- [x] Remove Library/Config files <!-- id: 3 -->
    - Removed `~/.npm/_npx/705d23756ff7dacc`
- [x] Verify uninstallation <!-- id: 4 -->

# Identify Installed MCPs

- [x] Search for running MCP processes <!-- id: 5 -->
    - Found `mcp-server-sequential-thinking`
- [x] Inspect npm/npx cache for MCP packages <!-- id: 6 -->
    - Found `mcp-server-sequential-thinking`
    - Found various `create-*` apps (not MCPs)
    - Investigating `e8d625d0f85748aa`
- [x] Check global npm packages <!-- id: 7 -->
    - Only `npm` and `corepack` found

- [ ] Analyze findings for login requirements <!-- id: 8 -->


