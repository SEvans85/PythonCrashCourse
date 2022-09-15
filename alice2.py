filename = 'alice.txt'

try:
    with open(filename, encoding='utf-8') as f:
        contents = f.read()
except FileNotFoundError:
    print(f'Sorry, file not found.')
else:
    #count the approximate number of words in the file
    words = contents.split()
    num_words = len(words)
    print(f'The file {filename} contains {num_words} words.')