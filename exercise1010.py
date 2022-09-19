filename = 'alice.txt'

try:
    with open(filename, encoding='utf-8') as f:
        contents = f.read()
        words = contents.split()
        print(contents.lower().count('the')) #any words that contain 'the' ie 'then' or 'there'
        print(contents.lower().count('the ')) #the word 'the' or words ending in 'the'

except FileNotFoundError:
    print('sorry, file does not exist')







