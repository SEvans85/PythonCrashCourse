from random import choice

list1 = [4, 7, 11, 16, 18, 22, 44, 32, 1, 50, 'a', 'f', 'k', 'n', 'y']
winner = []
print('The winning ticket is...')
while len(winner) < 4:
    item = choice(list1)
    if item not in winner:
        print(f'The first item is: {item}')
        winner.append(item)


