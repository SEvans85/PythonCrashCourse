def count_words(filename):
    """Count the approximate number of words in a file."""
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        print(f'Sorry, the file {filename} has not been found.')
    else:
        words = contents.split()
        num_words = len(words)
        print(f'the file {filename} has {num_words} words.')

filenames = ['alice.txt', 'Alex_Ferguson.txt', 'moby_dick.txt']

for file in filenames:
    count_words(file)
