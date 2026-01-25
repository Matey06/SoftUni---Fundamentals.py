numbers = input().split()
remeved_numbers = int(input())

int_numbers = []
for number in numbers:
    int_numbers.append(int(number))

int_numbers.sort(reverse=True)
after_removal = (int_numbers[:(len(int_numbers) - remeved_numbers)])



print(', '.join(map(str, after_removal)))