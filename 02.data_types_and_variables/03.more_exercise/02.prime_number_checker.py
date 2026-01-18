integer_number = int(input())

is_prime = False

if integer_number <= 1:
    print(is_prime)
else:
    for i in range(2,integer_number):
        if integer_number % i != 0:
            continue
        else:
            is_prime = True

if is_prime:
    print('False')
else:
    print('True')