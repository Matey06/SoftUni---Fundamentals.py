import re

text = input()

pattern = r'([|#])([a-z\s]+)\1([0-9]{2}\/[0-9]{2}\/[0-9]{2})\1([0-9]+)\1'
matches = re.findall(pattern, text, re.IGNORECASE)

total_calories = 0

for match in matches:
    calories = int(match[3])
    total_calories += calories

days_remaining = total_calories // 2000

print(f'You have food to last you for: {days_remaining} days!')

for match in matches:
    food, date, energy = match[1], match[2], match[3]
    print(f'Item: {food}, Best before: {date}, Nutrition: {energy}')
