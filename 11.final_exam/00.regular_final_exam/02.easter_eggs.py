import re

text = input()

pattern = r'[@#]+([a-z]{3,})[@#]+([^A-Za-z0-9]*)\/+([0-9]+)\/+'

matches = re.findall(pattern, text)

for match in matches:
    color = match[0]
    amount = match[2]
    print(f'You found {amount} {color} eggs!')
