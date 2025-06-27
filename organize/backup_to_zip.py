# backup_to_zip.py - Copies an entire folder and its contents into
# a zip file whose filename increments

import zipfile, os
from pathlib import Path

def backup_to_zip(folder):
    # Back up the entire contents of "folder" into a ZIP file.
    folder = Path(folder) # Make sure folder is a Path object, not a string.

    # Figure out the ZIP filename this code should use, based on
    # what files already exist
    number = 1
    while True:
        zip_filename = Path(folder.parts[-1] + '_' + str(number) + '.zip')
        if not zip_filename.exists():
            break
        number += 1

    # Create the ZIP file.
    print(f'Creating {zip_filename}...')
    zip_file = zipfile.ZipFile(zip_filename, 'w')

    # TODO: Walk the entire folder tree and compress the files in each folder.
    for folder_name, subfolders, filenames in os.walk(folder):
        folder_name = Path(folder_name)
        print(f'Adding files in folder {folder_name}...')

        # Add all the files in this folder to the ZIP file.
        for filename in filenames:
            print(f'Adding file {filename}...')
            zip_file.write(folder_name / filename)
    
    zip_file.close()
    print('Done.')

backup_to_zip(Path.cwd() / 'spam')