from pathlib import Path
import re

# Write a program that opens all .txt files in a folder and 
# searches for any line that matches a user-supplied regular 
# expression, then prints the results to the screen.

folder = Path.cwd()

user_regex = input("Enter your regular expression: ")
pattern = re.compile(user_regex)

for name in folder.glob('*'):
    if name.suffix == ".txt":
        with open(name, encoding='utf-8') as f_obj:
            contents = f_obj.readlines()
            for line in contents:
                print(''.join(pattern.findall(line)))