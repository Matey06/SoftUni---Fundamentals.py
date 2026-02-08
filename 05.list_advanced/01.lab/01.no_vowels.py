text = input()
vowels = ['a', 'e', 'i', 'o', 'u']
filtered_text = [letter for letter in text if letter.lower() not in vowels]
print(''.join(filtered_text))