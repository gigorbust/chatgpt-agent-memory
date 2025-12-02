# Implementation Plan - Drive Scanner & Archiver

This script will scan all accessible drives for files matching specific criteria and archive them to a GitHub repository.

## User Review Required

> [!IMPORTANT]
> **Target Repository**: I need to know the absolute path to your local "logs" GitHub repository. I will attempt to find it, but if I cannot, I will create a new directory `~/meztal_logs_archive` as a staging area.
> **Cloud Drives**: Ensure all CloudMounter drives are mounted and visible in `/Volumes`.
> **Exclusion Logic**: I will exclude files older than 6 months (approx May 2025) that contain "comparison", "senior", and "living" in their name.

## Proposed Changes

### Script Creation

#### [NEW] [scan_and_archive.py](file:///Users/georgegayl/.gemini/antigravity/scratch/scan_and_archive.py)
- **Functionality**:
    - Detects mounted volumes in `/Volumes`.
    - Recursively scans all files.
    - Filters for filenames containing "meztal" or "nearshoring" (case-insensitive).
    - Applies exclusion logic:
        - If file age > 6 months AND filename contains "comparison" + "senior" + "living" (fuzzy match), SKIP.
    - Copies matched files to the target repository, preserving directory structure to avoid collisions.
    - Performs `git add`, `git commit`, and `git push` (if target is a git repo).
    - Runs continuously until finished.
    - Handles permission errors gracefully.

## Verification Plan

### Automated Tests
- I will run the script on a small test directory first to verify filtering and copying logic.
- Command: `python3 scan_and_archive.py --test-mode` (I will implement a test mode or just run on a dummy folder).

### Manual Verification
- Check the target directory/repo to ensure files are copied.
- Verify that "senior living comparison" files older than 6 months are NOT present.
- Verify that "meztal" files ARE present.
