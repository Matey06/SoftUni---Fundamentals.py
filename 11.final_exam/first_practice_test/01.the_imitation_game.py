message = input()

instructions = input()

while instructions != 'Decode':

    if 'Move' in instructions:
        _, number_of_letters = instructions.split('|')
        number_of_letters = int(number_of_letters)
        message = message[number_of_letters:] + message[:number_of_letters]


    elif 'Insert' in instructions:
        _, index, value = instructions.split('|')
        index = int(index)
        message = message[:index] + value + message[index:]

    elif 'ChangeAll' in instructions:
        _, substring, replacement = instructions.split('|')
        message = message.replace(substring, replacement)

    instructions = input()


print(f'The decrypted message is: {message}')
