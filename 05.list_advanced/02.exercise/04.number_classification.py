numbers = list(map(int, input().split(', ')))
positive_list = [positive for positive in numbers if positive >= 0]
negative_list = [negative for negative in numbers if negative < 0]
even_list = [even for even in numbers if even % 2 == 0]
odd_list = [odd for odd in numbers if odd % 2 != 0]

positive_numbers = ', '.join(map(str, positive_list))
negative_numbers = ', '.join(map(str, negative_list))
even_numbers = ', '.join(map(str, even_list))
odd_numbers = ', '.join(map(str, odd_list))

print(f'Positive: {positive_numbers}')
print(f'Negative: {negative_numbers}')
print(f'Even: {even_numbers}')
print(f'Odd: {odd_numbers}')