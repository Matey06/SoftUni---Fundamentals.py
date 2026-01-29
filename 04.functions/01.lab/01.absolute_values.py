numbers = input().split()

float_numbers = [float(number) for number in numbers]

absolute_values = list(map(abs, float_numbers))

print(absolute_values)