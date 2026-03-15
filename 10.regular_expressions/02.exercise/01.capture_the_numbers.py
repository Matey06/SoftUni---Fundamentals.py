import re

text = input()

pattern = r'\d+'
numbers = []

while text:

    matches = re.findall(pattern, text)

    if matches:
        for num in matches:
            numbers.append(num)

    text = input()

print(*numbers)
