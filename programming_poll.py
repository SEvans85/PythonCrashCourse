filename = 'programming_poll.txt'

while True:
    why = input('Why do you like programming? ')
    with open(filename, 'a') as file_object:
        file_object.write(f'{why}\n')


