with open('pi_digits.txt') as file_object:
    contents = file_object.read()
print(contents)

with open('text_files/numbers.txt') as numbers_object:
    numbers = numbers_object.read()
print(numbers[3:7])