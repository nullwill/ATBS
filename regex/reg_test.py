import re

phrase = "Goodbyte, world! Hello, job! Goodbye!"
find = "Goodbye"

begins_with_hello = re.compile(f'{find}$!?')
if begins_with_hello.search(phrase):
    print(f"It does end with \"{find}\"!")
else:
    print(f"It does not end with \"{find}\"")