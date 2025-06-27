file_obj = open('data.txt', 'w', encoding='utf-8')
file_obj.write('Hello, world!')
file_obj.close()
file_obj = open('data.txt', encoding='utf-8')
content = file_obj.read()
file_obj.close()

print(content)

with open('data.txt', 'w', encoding='utf-8') as file_obj:
    file_obj.write('Hello, world!')
with open('data.txt', encoding='utf-8') as file_obj:
    content = file_obj.read()

print(content)