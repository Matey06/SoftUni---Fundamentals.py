numbers = [int(num) for num in input().split()]

average_lst_value = sum(numbers) / len(numbers)

greatest_numbers = []

for num in numbers:

    if num > average_lst_value:
        greatest_numbers.append(num)

if not greatest_numbers:
    print('No')
else:
    greatest_numbers.sort(reverse=True)
    greatest_five = greatest_numbers[:5]
    print(*greatest_five)