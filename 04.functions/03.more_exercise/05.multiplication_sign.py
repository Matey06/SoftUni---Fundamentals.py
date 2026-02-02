numbers = []

for _ in range(3):
    num = int(input())
    numbers.append(num)

negative_counter = 0

for number in numbers:
    if number == 0:
        print('zero')
        break
    elif number < 0:
        negative_counter += 1
else:
    if negative_counter % 2 != 0:
        print('negative')
    else:
        print('positive')