filenames = ['dogs.txt', 'birds', 'cats.txt']

for file in filenames:
    try:
        with open(file, encoding='utf-8') as f:
            contents = f.read()
        print(contents)

    except FileNotFoundError:
        print(f'Sorry file {file} has not been found.')


