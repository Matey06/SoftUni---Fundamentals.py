coded_message = input()

new_message = ''

command = input()

while command != 'Finalize':

    if command == 'Encrypt':
        coded_message = coded_message[::-1]
        print(coded_message)

    elif command == 'Decrypt':
        for char in coded_message:
            if char.isalpha():
                if char.isupper():
                    new_message += char.lower()
                else:
                    new_message += char.upper()
            else:
                new_message += char
        coded_message = new_message
        new_message = ''
        print(coded_message)

    elif command.startswith('Substitute'):
        _, old_char, new_char = command.split(' ')
        if old_char in coded_message:
            coded_message = coded_message.replace(old_char, new_char)
            print(coded_message)
        else:
            print('Character not found.')

    elif command.startswith('Scramble'):
        _, index, char = command.split(' ')
        index = int(index)
        if 0 <= index < len(coded_message):
            for i in range(0, len(coded_message)):
                if i == index:
                    new_message += char
                else:
                    new_message += coded_message[i]
            coded_message = new_message
            new_message = ''
            print(coded_message)
        else:
            print('Index out of bounds.')

    elif command.startswith('Remove'):
        _, substring = command.split(' ', 1)
        if substring in coded_message:
            coded_message = coded_message.replace(substring, "")
            print(coded_message)
        else:
            print(coded_message)
    else:
        print('Invalid command detected!')

    command = input()
