filename = 'text_files/learning_python.txt'

with open(filename) as file_object:
    contents = file_object.read()

print(f'{contents}\n' * 3)


with open(filename) as file_objectlines:
    contentslines = file_objectlines.readlines()


i = 0
while i < 3:
    for line in contentslines:
        print(line.replace('Python', 'C++'))
    print(f'\n')
    i +=1




    
