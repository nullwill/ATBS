from pathlib import Path
import re, os, shutil

# dateConversion.py - Searches all filenames in the current working directory and all
# subdirectories and identifies filenames with the MM-DD-YYYY pattern in them. For example
# spam12-31-1900.txt. Assumes the months and days always use two digits, and that files with 
# non-existent dates do not exist (i.e. 99-99-9999.txt). When a filename is found, it is 
# renamed in the format DD-MM-YYYY

p = Path.cwd()


date_re = re.compile(r'(\d{2})-(\d{2})-(\d{4})')

for folder_name, subfolders, filenames in os.walk(p):
    for filename in filenames:
        if date_re.search(filename):
            new_filename = date_re.sub(r'\2-\1-\3', filename)
            source_file = Path(folder_name) / filename
            dest_file = Path(folder_name) / new_filename
            print(f'Changing "{filename}" to "{new_filename}"...')
            shutil.move(source_file, dest_file)
