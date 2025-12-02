# Walkthrough - Drive Scanning & Archiving

I have created and executed a script to scan your drives for "meztal" related files and archive them to a git repository.

## What was done
1.  **Explored Environment**: Checked for mounted drives and existing logs repository.
2.  **Created Script**: Developed `scan_and_archive.py` to:
    -   Scan `/Volumes` and `~` (Home Directory).
    -   Filter for files containing "meztal" or "nearshoring".
    -   Exclude "senior living comparison" files older than 6 months.
    -   Copy relevant files to `~/meztal_logs_archive`.
    -   Commit and push changes (if a remote is configured later).
3.  **Executed Scan**: Ran the script to perform the initial scan and archive.

## Verification Results

### Automated Scan
The script runs automatically and logs its progress.
-   **Target Repo**: `~/meztal_logs_archive`
-   **Scan Scope**: All mounted volumes and home directory.

### Manual Verification
You can verify the results by checking the archive folder:
```bash
ls -R ~/meztal_logs_archive
```

## Next Steps
-   If you have a remote URL for the logs repo, you can add it:
    ```bash
    cd ~/meztal_logs_archive
    git remote add origin <url>
    git push -u origin main
    ```
