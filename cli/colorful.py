from pathlib import Path
import os, bext, time

bext.fg('green')

p = Path.home()

for folder_name, subfolders, filenames in os.walk(p):
    print(f"Current folder: {folder_name}")

    tabs = len(folder_name.split('/'))
    for filename in filenames:
        print(filename)
    
    time.sleep(.1)
    # for subfolder in subfolders:
    #     print(f"Subfolder of {folder_name}: {subfolder}")

    # for filename in filenames:
    #     print(f"File in {folder_name}: {filename}")
    