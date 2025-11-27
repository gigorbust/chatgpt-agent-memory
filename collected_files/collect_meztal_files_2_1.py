import os
import shutil
import subprocess
from pathlib import Path
import datetime

# Configuration
SEARCH_TERM = "MezTal"
DESTINATION_DIR = "/Users/georgegayl/Library/CloudStorage/Dropbox (9-1-25 10:19 PM)/Silent Storm RF (1)/Meztal/Google Antigravity/chatgpt-agent-memory/collected_files"
SOURCE_ROOT = "/Users/georgegayl"  # Search scope (effectively ignored by mdfind which searches indexed locations, but useful for filtering if needed)

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

def collect_files():
    print(f"--- Starting Collection for '{SEARCH_TERM}' ---")
    print(f"Destination: {DESTINATION_DIR}")
    
    # Create destination if it doesn't exist
    if not os.path.exists(DESTINATION_DIR):
        os.makedirs(DESTINATION_DIR)
        print(f"Created directory: {DESTINATION_DIR}")

    # Use mdfind (Spotlight) for fast search
    try:
        print("Searching with mdfind (Spotlight)...")
        # -name is case-insensitive by default in mdfind? No, usually case-insensitive.
        # Using 'kMDItemDisplayName == "*MezTal*"c' for explicit case-insensitivity if needed, 
        # but 'mdfind -name MezTal' is usually sufficient and simpler.
        result = subprocess.run(['mdfind', '-name', SEARCH_TERM], capture_output=True, text=True)
        paths = result.stdout.strip().split('\n')
    except Exception as e:
        print(f"Error running mdfind: {e}")
        return

    print(f"Found {len(paths)} items.")
    
    count = 0
    skipped = 0
    errors = 0

    for path_str in paths:
        if not path_str:
            continue
            
        source_path = Path(path_str)
        
        # SKIP CHECKS
        
        # 1. Skip if it's a directory (we only want files, or should we copy folders? Usually files is safer for 'documents')
        if not source_path.is_file():
            # print(f"Skipping directory: {source_path}")
            continue
            
        # 2. Skip if it's already in the destination folder (prevent self-replication)
        if DESTINATION_DIR in str(source_path.parent):
            # print(f"Skipping file already in destination: {source_path}")
            continue
            
        # 3. Skip if it's in a hidden folder or system folder that might be irrelevant (optional, but good for noise reduction)
        # For now, we'll copy everything to be safe as requested "everywhere".
        
        try:
            filename = source_path.name
            unique_name = get_unique_filename(DESTINATION_DIR, filename)
            dest_path = os.path.join(DESTINATION_DIR, unique_name)
            
            shutil.copy2(source_path, dest_path)
            print(f"Copied: {filename} -> {unique_name}")
            count += 1
            
        except Exception as e:
            print(f"Failed to copy {source_path}: {e}")
            errors += 1

    print(f"--- Finished ---")
    print(f"Total copied: {count}")
    print(f"Errors: {errors}")

if __name__ == "__main__":
    collect_files()
