encoded_strings = input().split()

total_score = 0

for current_string in encoded_strings:

    first_letter = current_string[0]
    last_letter = current_string[-1]
    num = ''
    for char in current_string:
        if char.isdigit():
            num += char

    number = int(num)

    if first_letter == first_letter.upper():
        number /= ord(first_letter) - 64
    else:
        number *= ord(first_letter) - 96

    if last_letter == last_letter.upper():
        number -= ord(last_letter) - 64
    else:
        number += ord(last_letter) - 96

    total_score += number

print(f"{total_score:.2f}")
