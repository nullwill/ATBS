import os, shutil
from pathlib import Path
c = Path.cwd()

for folder_name, subfolders, filenames in os.walk(c / 'spam'):
    print('The current folder is ' + folder_name)

    for subfolder in subfolders:
        print('SUBFOLDER OF ' + folder_name + ': ' + subfolder)
    
    for filename in filenames:
        print('FILE INSIDE ' + folder_name + ': ' + filename)
        # Rename file to uppercase:
        # p = Path(folder_name)
        # shutil.move(p / filename, p / filename.upper())
    
    print('')