n = int(input())

for number in range(1, n + 1):

    number_sum = 0

    for digit in str(number):

        number_sum += int(digit)

    if number_sum == 5 or number_sum == 7 or number_sum == 11:
        print(f'{number} -> True')
    else:
        print(f'{number} -> False')