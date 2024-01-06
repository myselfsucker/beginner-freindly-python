from pyperclip import paste

text = paste()

text = text.split('\n')

new_format = []
for i in text:
        i = f'* {i}'

        new_format.append(i)
         
result = '\n'.join(new_format)

print(result)