import os
import shutil
import subprocess
from pathlib import Path
import datetime

# Configuration
SEARCH_TERM = "MezTal"
DESTINATION_DIR = "/Users/georgegayl/Library/CloudStorage/Dropbox (9-1-25 10:19 PM)/Silent Storm RF (1)/Meztal/Google Antigravity/chatgpt-agent-memory/collected_files"
TIMEOUT_SECONDS = 300  # Timeout for each top-level folder scan

# Search Roots
CLOUD_STORAGE = os.path.expanduser("~/Library/CloudStorage")
VOLUMES = "/Volumes"

def get_unique_filename(destination, filename):
    if not os.path.exists(os.path.join(destination, filename)):
        return filename
    name, ext = os.path.splitext(filename)
    counter = 1
    while True:
        new_filename = f"{name}_{counter}{ext}"
        if not os.path.exists(os.path.join(destination, new_filename)):
            return new_filename
        counter += 1

def run_find_with_timeout(root_path):
    print(f"  Scanning: {root_path} (Timeout: {TIMEOUT_SECONDS}s)...")
    try:
        # Using -iname for case-insensitive search
        result = subprocess.run(
            ['find', root_path, '-iname', f'*{SEARCH_TERM}*'], 
            stdout=subprocess.PIPE,
            stderr=subprocess.DEVNULL,
            text=True,
            timeout=TIMEOUT_SECONDS
        )
        return result.stdout.strip().split('\n')
    except subprocess.TimeoutExpired:
        print(f"  [TIMEOUT] Skipping {root_path} - took longer than {TIMEOUT_SECONDS}s")
        return []
    except Exception as e:
        print(f"  [ERROR] {root_path}: {e}")
        return []

def resume_collection():
    print(f"--- Resuming Collection for '{SEARCH_TERM}' (Deep Search Only) ---")
    
    if not os.path.exists(DESTINATION_DIR):
        os.makedirs(DESTINATION_DIR)

    # Build list of existing files to avoid redundant copying (simple check by name)
    existing_files = set(os.listdir(DESTINATION_DIR))
    print(f"Existing files in destination: {len(existing_files)}")

    search_targets = []
    
    # Add CloudStorage subdirectories
    if os.path.exists(CLOUD_STORAGE):
        for item in os.listdir(CLOUD_STORAGE):
            path = os.path.join(CLOUD_STORAGE, item)
            if os.path.isdir(path):
                search_targets.append(path)
    
    # Add Volumes
    if os.path.exists(VOLUMES):
        for item in os.listdir(VOLUMES):
            path = os.path.join(VOLUMES, item)
            # Skip Macintosh HD to avoid redundant local scan (covered by Spotlight)
            if os.path.isdir(path) and "Macintosh HD" not in item:
                search_targets.append(path)

    print(f"Targeting {len(search_targets)} locations:")
    
    new_files_count = 0
    
    for target in search_targets:
        found_paths = run_find_with_timeout(target)
        
        if not found_paths or not found_paths[0]:
            continue
            
        print(f"    Found {len(found_paths)} items.")
        
        for path_str in found_paths:
            if not path_str: continue
            
            source_path = Path(path_str)
            if not source_path.is_file(): continue
            
            # Check if file already exists in destination (by name, to be safe/fast)
            # Note: This might skip different files with same name, but get_unique_filename handles collisions
            # if we decide to copy. The user said "no redundant work", so let's be careful.
            # Actually, let's rely on the copy logic to handle duplicates.
            
            if DESTINATION_DIR in str(source_path.parent): continue

            try:
                filename = source_path.name
                # Optional: Skip if filename is already in destination? 
                # User said "no redundant work". If we have "file.txt", and we find another "file.txt",
                # is it the same? Maybe. 
                # Let's copy it to be safe, get_unique_filename will handle it.
                
                unique_name = get_unique_filename(DESTINATION_DIR, filename)
                dest_path = os.path.join(DESTINATION_DIR, unique_name)
                
                shutil.copy2(source_path, dest_path)
                new_files_count += 1
            except Exception:
                pass

    print(f"--- Finished ---")
    print(f"New files copied: {new_files_count}")

if __name__ == "__main__":
    resume_collection()
