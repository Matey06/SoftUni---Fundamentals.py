import re

coolness = 1

text = input()
for char in text:
    if char.isdigit():
        coolness *= int(char)

pattern = r'(\*\*|::)([A-Z][a-z]{2,})\1'

matches = re.findall(pattern, text)

all_emojis = {}

for match in matches:
    ascii_value = 0
    for char in match[1]:
        ascii_value += ord(char)
    all_emojis[match[1]] = [match[0], ascii_value]

print(f'Cool threshold: {coolness}')
print(f'{len(all_emojis)} emojis found in the text. The cool ones are:')

for emoji, values in all_emojis.items():
    if values[1] >= coolness:
        print(f'{values[0]}{emoji}{values[0]}')
