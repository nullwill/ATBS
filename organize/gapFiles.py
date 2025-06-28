from pathlib import Path
import os, re, shutil

# gapFiles.py - Inserts gaps into numbered files and bumps up the numbers in the
# filenames after the gap, so that a new file can be inserted.

prefix = "spam"

p = Path.cwd() / 'spam'

files = sorted(os.listdir(p))

number_patt = re.compile(r'\d+')
pattern = re.compile(f'^{prefix}')

matches = [file for file in files if pattern.match(file)]

i = int(number_patt.search(matches[0]).group())

# gap = []

# while True:
#     number = input("Enter a number to gap: ")
#     if not number:
#         break
#     gap.append(int(number))

gap = 9
flag = False

for file in matches:
    print(f"processing {file}")
    if (int(number_patt.search(file).group())) == gap:
        i += 1
    if (int(number_patt.search(file).group())) != i:
        src_file = p / file
        dest_file = p / f'{prefix}{str(i).zfill(3)}.txt'
        shutil.move(src_file, dest_file)
        print(f"Moving {src_file} to {dest_file}")
    print('')
    i += 1
