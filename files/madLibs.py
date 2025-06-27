import re

with open('mad_libs.txt', encoding='utf-8') as file_obj:
    contents = file_obj.read()

user_re = re.compile('ADJECTIVE|NOUN|VERB|ADVERB')

def replace_placeholder(match):
    word_type = match.group()
    article = 'an' if word_type[0] in 'AEIOU' else 'a'
    user_input = input(f"Enter {article} {word_type.lower()}: ")
    return user_input

result = user_re.sub(replace_placeholder, contents)

print("Result:")
print(result)