# extensionCopy.py - Walks through a folder tree and searches for files with 
# certain file extensions (such as .pdf or .jpg) and copies these files from
# their current location to a new folder.

from pathlib import Path
import shutil, os

p = Path.cwd() # Default path is current working directory
ext = ".txt"   # Default file extension is .txt
dest_folder = Path.cwd() / 'txt_backup'

user_input = input("Enter an extension to search for: ")
if len(user_input) > 0:
    ext = "." + user_input
    dest_folder = Path.cwd() / f'{user_input}_backup'
else:
    print("Defaulting to .txt")
print(f"Creating destination folder: {dest_folder}")

dest_folder.mkdir(exist_ok=True)

for folder_name, subfolders, filenames in os.walk(p):
    for filename in Path(folder_name).glob('*' + ext):
        print(filename.name)
        print(os.listdir(dest_folder))
        if filename.name in os.listdir(dest_folder):
            shutil.copy(filename, f'{dest_folder}/{filename.stem}_cpy{filename.suffix}')
        else:
            shutil.copy(filename, dest_folder)
        print(f'Copying {filename} to {dest_folder}')