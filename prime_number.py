
flag = False

def is_prime(num):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                print(f'number {num} is divisible by {i}.')
                break;
        else:
            print(f'{num} is a prime number.')
    else:
        print(f'{num} is not a prime number.')



for k in range(1,50):
    is_prime(k)