message = input()

command = input()
while command != 'Reveal':

    if 'InsertSpace' in command:
        _, index = command.split(':|:')
        index = int(index)
        message = message[:index] + ' ' + message[index:]
        print(message)

    elif 'Reverse' in command:
        _, substring = command.split(':|:')
        if substring in message:
            message = message.replace(substring, '', 1)
            reversed_substring = substring[::-1]
            message += reversed_substring
            print(message)
        else:
            print('error')

    elif 'ChangeAll' in command:
        _, substring, replacement = command.split(':|:')
        if substring in message:
            message = message.replace(substring, replacement)
            print(message)

    command = input()

print(f'You have a new text message: {message}')
