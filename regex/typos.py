import re

repeated_re = re.compile(r'(\b\w+\b)\s+\1', re.I)
spaces_re   = re.compile(r'\s{2,}')
punctuation_re = re.compile(r'!{2,}')

text = "Find common typos, such as multiple spaces between words, offset accIdentally    accidEntally! repeated words, or multiple exclamation marks at the ends of sentences. Those are annoying!?!"

print(repeated_re.findall(text))
print(spaces_re.search(text))
print(punctuation_re.search(text))