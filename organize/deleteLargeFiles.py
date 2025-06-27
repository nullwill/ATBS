from pathlib import Path
import shutil, os

MB = 1024 * 1024
delete_size = 100 * MB # Delete files greater than 100 MB
print(delete_size)

p = Path.cwd()
print(p)

for folder_name, subfolders, filenames in os.walk(p):
    for filename in filenames:
        path = Path(folder_name) / filename
        print(f"{path} is {os.path.getsize(path)/MB:.2f} MB")
        if os.path.getsize(path) > delete_size:
            print(f"Deleting {path}...")
            os.unlink(path)