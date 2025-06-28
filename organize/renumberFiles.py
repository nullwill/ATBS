from pathlib import Path
import os, re, shutil

# rememberFiles.py - Find all files with a given prefix, such as spam001.txt,
# spam002.txt, and so on, in a single folder and locates any gaps in the numbering
# (such as if there is a spam001.txt and a spam003.txt but no spam002.txt). The
# program rename all later files to close the gap.

prefix = "spam"

p = Path().cwd() / 'spam'

files = sorted(os.listdir(p))

matches = []

number_patt = re.compile(r'\d+')
prev_num = 0

pattern = re.compile(f'^{prefix}')
for file in files:
    if pattern.match(file):
        matches.append(file)

i = int(number_patt.search(matches[0]).group())

for file in matches:
    if int(number_patt.search(file).group()) != i:
        print(f"Processing {file}")
        src_file = p / file
        dest_file = p / f'{prefix}{str(i).zfill(3)}.txt'
        print(f"Moving {src_file} to {dest_file}...")
        shutil.move(p / file, p / f'{prefix}{str(i).zfill(3)}.txt')
    i += 1
