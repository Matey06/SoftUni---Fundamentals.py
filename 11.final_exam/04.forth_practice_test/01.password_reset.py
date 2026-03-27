text = input()

modified_text = ''

command = input()

while command != 'Done':

    if command == 'TakeOdd':
        modified_text = ''
        for i in range(len(text)):
            if i % 2 != 0:
                modified_text += text[i]
        text = modified_text
        print(text)

    elif 'Cut' in command:
        _, index, length = command.split(' ')
        index = int(index)
        length = int(length)
        text = text[:index] + text[index + length:]
        print(text)

    elif 'Substitute' in command:
        _, substring, substitute = command.split(' ')
        if substring in text:
            text = text.replace(substring, substitute)
            print(text)
        else:
            print('Nothing to replace!')

    command = input()

print(f'Your password is: {text}')
