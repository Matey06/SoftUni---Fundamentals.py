messages = input().split()

new_messages = []

unique_symbols = 0

index = -1

number = ''

for message in messages:
    new_message = ''
    index += 1
    new_messages.append('')

    for char in message:

        if char.isalpha() or not char.isalnum():

            if number:
                new_message *= int(number)
                new_messages[index] += new_message
                number = ''
                new_message = ''

            if char not in new_message and char.upper() not in new_messages[index]:
                unique_symbols += 1
            new_message += char.upper()
            continue

        if char.isdigit():
            number += char

    if number:
        new_message *= int(number)
        new_messages[index] += new_message
        number = ''

print(f'Unique symbols used: {unique_symbols}')
print(' '.join(new_messages))
