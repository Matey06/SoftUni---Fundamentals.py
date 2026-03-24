import re

text = input()

pattern = r'([@#])([A-Za-z]{3,})\1{2}([A-Za-z]{3,})\1'

matches = re.findall(pattern, text)

mirror_words = []

for match in matches:
    first_half = match[1]
    second_half = match[2]
    if first_half == second_half[::-1]:
        mirror_words.append(first_half + ' <=> ' + second_half)


if matches:
    print(f'{len(matches)} word pairs found!')
else:
    print(f'No word pairs found!')


if mirror_words:
    print('The mirror words are:')
    print(', '.join(mirror_words))
else:
    print('No mirror words!')
