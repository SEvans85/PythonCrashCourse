filename = 'text_files/pi_1million.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(f'{pi_string[:52]}...')
print(len(pi_string))

birthday = input('Enter your birthday in the format ddmmyy: ')

if birthday in pi_string:
    print('Wow, your birthday appears in the first million digits in pi.')
else:
    print('Aww, your birthday does not appear in the first million digits in pi.')



