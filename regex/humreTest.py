import re

PERIOD = "\."

floating_re = re.compile(r'\d' + PERIOD + r'\d')
print(floating_re.search("Find the floating point 5A6 number!!"))