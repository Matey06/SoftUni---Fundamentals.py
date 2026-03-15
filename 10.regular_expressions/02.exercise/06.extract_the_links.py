import re

text = input()

pattern = r'\b((w{3})\.([a-z0-9\-]+)(\.[a-z]+)+)'

while text:

    match = re.search(pattern, text, re.IGNORECASE)

    if match:
        print(match[0])

    text = input()
