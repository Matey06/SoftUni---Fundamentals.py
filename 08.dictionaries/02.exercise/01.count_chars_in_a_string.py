text = input().split()

letters = {}

for word in text:
    for char in word:
        if char not in letters:
            letters[char] = 1
        else:
            letters[char] += 1

for letter, count in letters.items():
    print(f'{letter} -> {count}')
