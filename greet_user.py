import json

filename = 'username.txt'

with open(filename) as f:
    username = json.load(f)
    print(f'Welcome back, {username}!')