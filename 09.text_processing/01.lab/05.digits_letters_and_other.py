text = input()

characters = ''
digits = ''
symbols = ''

for char in text:
    if char.isdigit():
        digits += char

    elif char.isalpha():
        characters += char

    else:
        symbols += char

print(f'{digits}\n{characters}\n{symbols}')
