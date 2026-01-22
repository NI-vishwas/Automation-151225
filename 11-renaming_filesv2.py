# Renaming files using pathlib module
from pathlib import Path
from datetime import datetime as dt 

BASE_DIR = Path('/home/vishwas/Workspace/dummy2/') ## Change the base dir
TARGET_EXTENSIONS = {".txt"}

for file_path in BASE_DIR.glob("*"):
    if file_path.suffix.lower() in TARGET_EXTENSIONS:
        mtime = file_path.stat().st_mtime
        date_str = dt.fromtimestamp(mtime).strftime('%Y-%m-%d_%H%M%S')
        new_name = f"{date_str}_{file_path.name}" 
        file_path.rename(BASE_DIR / new_name)
        print(f"Renamed file: {file_path.name}")
    else:
        print(f"Skipping: {file_path.name}, file type not targeted")

