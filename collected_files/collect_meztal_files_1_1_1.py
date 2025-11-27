import os
import shutil
import subprocess
from pathlib import Path
import datetime

# Configuration
SEARCH_TERM = "MezTal"
DESTINATION_DIR = "/Users/georgegayl/Library/CloudStorage/Dropbox (9-1-25 10:19 PM)/Silent Storm RF (1)/Meztal/Google Antigravity/chatgpt-agent-memory/collected_files"

# Search Roots
USER_HOME = "/Users/georgegayl"
CLOUD_STORAGE = os.path.expanduser("~/Library/CloudStorage")
VOLUMES = "/Volumes"

def get_unique_filename(destination, filename):
    """
    Generates a unique filename if the file already exists in the destination.
    Appends _1, _2, etc.
    """
    if not os.path.exists(os.path.join(destination, filename)):
        return filename
    
    name, ext = os.path.splitext(filename)
    counter = 1
    while True:
        new_filename = f"{name}_{counter}{ext}"
        if not os.path.exists(os.path.join(destination, new_filename)):
            return new_filename
        counter += 1

def run_find_command(root_path):
    """Runs the 'find' command for a deep search."""
    print(f"  [Deep Search] Scanning: {root_path} (this may take a while)...")
    try:
        # find <path> -name "*MezTal*"
        # Using -iname for case-insensitive
        result = subprocess.run(
            ['find', root_path, '-iname', f'*{SEARCH_TERM}*'], 
            capture_output=True, 
            text=True,
            stderr=subprocess.DEVNULL # Suppress permission errors
        )
        return result.stdout.strip().split('\n')
    except Exception as e:
        print(f"  Error running find on {root_path}: {e}")
        return []

def collect_files():
    print(f"--- Starting Expanded Collection for '{SEARCH_TERM}' ---")
    print(f"Destination: {DESTINATION_DIR}")
    
    if not os.path.exists(DESTINATION_DIR):
        os.makedirs(DESTINATION_DIR)
        print(f"Created directory: {DESTINATION_DIR}")

    all_paths = set()

    # 1. Spotlight Search (Fast, Indexed)
    print("\n--- Phase 1: Spotlight Search (mdfind) ---")
    try:
        print("Running mdfind globally...")
        result = subprocess.run(['mdfind', '-name', SEARCH_TERM], capture_output=True, text=True)
        spotlight_paths = result.stdout.strip().split('\n')
        print(f"mdfind found {len(spotlight_paths)} items.")
        all_paths.update(p for p in spotlight_paths if p)
    except Exception as e:
        print(f"Error running mdfind: {e}")

    # 2. Deep Search (Slow, Manual Traversal)
    print("\n--- Phase 2: Deep Search (find) on Cloud & Volumes ---")
    
    # Identify search targets
    search_targets = []
    
    # Add CloudStorage subdirectories
    if os.path.exists(CLOUD_STORAGE):
        for item in os.listdir(CLOUD_STORAGE):
            path = os.path.join(CLOUD_STORAGE, item)
            if os.path.isdir(path):
                search_targets.append(path)
    
    # Add Volumes (excluding Macintosh HD to avoid double scan if possible, but safe to scan)
    if os.path.exists(VOLUMES):
        for item in os.listdir(VOLUMES):
            # Skip main drive if it's just a symlink or the root, but /Volumes/Macintosh HD is usually the mount.
            # We'll scan everything in /Volumes to be safe.
            path = os.path.join(VOLUMES, item)
            if os.path.isdir(path):
                search_targets.append(path)

    print(f"Targeting {len(search_targets)} locations for deep search:")
    for t in search_targets:
        print(f" - {t}")

    for target in search_targets:
        found = run_find_command(target)
        if found and found[0]:
            print(f"  Found {len(found)} items in {target}")
            all_paths.update(p for p in found if p)
        else:
            print(f"  No items found in {target}")

    # 3. Process & Copy
    print(f"\n--- Phase 3: Processing {len(all_paths)} Unique Paths ---")
    
    count = 0
    errors = 0

    for path_str in all_paths:
        if not path_str:
            continue
            
        source_path = Path(path_str)
        
        # Skip directories
        if not source_path.is_file():
            continue
            
        # Skip if already in destination
        if DESTINATION_DIR in str(source_path.parent):
            continue
            
        try:
            filename = source_path.name
            unique_name = get_unique_filename(DESTINATION_DIR, filename)
            dest_path = os.path.join(DESTINATION_DIR, unique_name)
            
            shutil.copy2(source_path, dest_path)
            # print(f"Copied: {filename}") # Reduce noise
            count += 1
            
        except Exception as e:
            # print(f"Failed to copy {source_path}: {e}")
            errors += 1

    print(f"--- Finished ---")
    print(f"Total copied: {count}")
    print(f"Errors: {errors}")

if __name__ == "__main__":
    collect_files()
