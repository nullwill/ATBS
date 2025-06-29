from pathlib import Path
import os, re, shutil

# gapFiles.py - Inserts gaps into numbered files and bumps up the numbers in the
# filenames after the gap, so that a new file can be inserted.

prefix = "spam"

p = Path.cwd() / 'spam'

files = sorted(os.listdir(p), reverse=True)

number_patt = re.compile(r'\d+')
pattern = re.compile(f'^{prefix}')

matches = [file for file in files if pattern.match(file)]


print(matches)

# gap = []

# while True:
#     number = input("Enter a number to gap: ")
#     if not number:
#         break
#     gap.append(int(number))

gap = [9, 10, 11]

i = int(number_patt.search(matches[0]).group()) + len(gap)

print(i)

for file in matches:
    print(f"processing {file}")
    file_number = int(number_patt.search(file).group())
    src_file = p / file
    dest_file = p / f'{prefix}{str(i).zfill(3)}.txt'
    shutil.move(src_file, dest_file)
    print(f"Moving {src_file} to {dest_file}")
    i -= 1
    if i in gap:
        i -= 1
    print('')
