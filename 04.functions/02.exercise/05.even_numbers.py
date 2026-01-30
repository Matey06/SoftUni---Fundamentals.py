numbers = input().split()
int_numbers = [int(number) for number in numbers]
even_numbers = list(filter(lambda x: x % 2 == 0, int_numbers))

print(even_numbers)