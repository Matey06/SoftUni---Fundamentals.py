import re

email = input()

pattern = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"

validator = re.match(pattern, email)

if validator:
    print(f"{email} is Valid!")
else:
    print(f"{email} is Invalid!")