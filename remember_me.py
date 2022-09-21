import json

username = input('What is your name? ')

filename = 'username.txt'
with open(filename, 'w') as f:
    json.dump(username, f)
    print(f'We will remember you when you come back, {username}!')