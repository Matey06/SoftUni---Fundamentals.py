numbers = input().split()

float_numbers = list(map(float, numbers))

rounded_numbers = list(map(round, float_numbers))
print(rounded_numbers)