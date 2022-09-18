#10.6 Addition

def numbers():
    num1 = input('Enter a number: ')
    num2 = input('Enter a number: ')

    try:
        print(int(num1) + int(num2))
    except ValueError:
        print('You did not enter 2 numbers')

numbers()


