numbers = input().split()
removed_numbers = int(input())

int_numbers = []
for number in numbers:
    int_numbers.append(int(number))

lst_copy = int_numbers.copy()
lst_copy.sort(reverse=True)

for _ in range(removed_numbers):

    lst_copy.pop()

filtered_lst = []

for element in int_numbers:

    if element in lst_copy:
        filtered_lst.append(element)

print(', '.join(map(str, filtered_lst)))