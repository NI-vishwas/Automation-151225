# Renaming files using os module
# os modules treats paths as strings
import os
from datetime import datetime as dt 

BASE_DIR = '/home/vishwas/Workspace/dummy1/' ## Change the base dir

def main():
    # 1. Check if the directory exists
    if not os.path.isdir(BASE_DIR):
        print(f"{BASE_DIR} does not exist or is not a directory")
    
    # 2. list all the files in directory
    for filename in os.listdir(BASE_DIR):
        # 3. Construct old_path
        old_path = os.path.join(BASE_DIR, filename)

        # if filename.endswith(".txt")
        # 4. We want to reanme only the files
        if os.path.isfile(old_path):
            timestamp = os.path.getmtime(old_path)
            date_str = dt.fromtimestamp(timestamp).strftime('%Y-%m-%d_%H%M%S')

            # 5. Create a new name
            # original name: abc.txt
            # modified at: 22 Jan 2026 8.00 PM 
            # new_name : 2026-01-22_200000_abc.txt
            new_name = f"{date_str}_{filename}" 
            new_path = os.path.join(BASE_DIR,new_name)

            # 6. Perform the renaming
            os.rename(old_path, new_path)
            print(f"Renamed: {filename} -> {new_name}")


if __name__ == '__main__':
    main()