import re

long_string = input()
key_word = input()

pattern = fr'\b{key_word}\b'

matches = re.findall(pattern, long_string, re.IGNORECASE)

print(len(matches))
