numbers = list(map(int, input().split(', ')))
copy = numbers.copy()

group_number = 10
start = 1
finish = 11

while copy:

    for current_number in range(len(numbers)):

        current_group = [num for num in numbers if num in range(start, finish)]

    print(f'Group of {group_number}\'s: {current_group}')

    for number in current_group:
        copy.remove(number)

    group_number += 10
    start += 10
    finish += 10