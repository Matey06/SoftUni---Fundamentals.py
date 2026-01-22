random_string_numbers = input().split()

flipped_numbers = []

for number in random_string_numbers:

    flipped_numbers.append(-int(number))

print(flipped_numbers)