#10.7 Addition Calculator

while True:
    try:
        num1 = input('Give me a number: ')
        num1 = int(num1)

        num2 = input('Give me a number: ')
        num2 = int(num2)

    except ValueError:
        print('Sorry, i need two numbers')

    else:
        sum = num1 + num2
        print(f'The sum of {num1} and {num2} is {sum}')