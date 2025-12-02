# Uninstall Atlassian Software Plan

## Goal Description
The user wants to "uninstall atlassian". Based on investigation, there are no standard Atlassian applications (like Jira or SourceTree) installed in `/Applications`. However, there are active `mcp-remote` processes connecting to `atlassian.com`, running from the `npm` `_npx` cache. The goal is to stop these processes and remove the cached files.

## User Review Required
- **Confirmation**: Confirm if the user intends to stop the MCP server processes.
- **Scope**: Confirm if there are other Atlassian tools they expect to be removed that we haven't found yet.

## Proposed Changes
### System
- **Processes**: Kill all `mcp-remote` processes related to Atlassian.
- **Files**: Remove the specific `npx` cache directories containing the Atlassian MCP server code.
    - Path: `/Users/georgegayl/.npm/_npx/705d23756ff7dacc` (and others if found)

## Verification Plan
### Automated Tests
- Run `ps aux | grep -i atlassian` to ensure no processes are running.
- Run `find ~/.npm/_npx -name "*atlassian*"` to ensure files are removed.
