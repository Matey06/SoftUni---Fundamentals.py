message = input()

message_letter_by_letter = [char for char in message]

instructions = input()

while instructions != 'Decode':

    if 'Move' in instructions:
        order, number_of_letters = instructions.split('|')
        for change in range(int(number_of_letters)):
            moved_element = message_letter_by_letter.pop(0)
            message_letter_by_letter.append(moved_element)

    elif 'Insert' in instructions:
        order, index, value = instructions.split('|')
        index = int(index)
        message_letter_by_letter.insert(index, value)

    elif 'ChangeAll' in instructions:
        order, substring, replacement = instructions.split('|')
        repetitions = message_letter_by_letter.count(substring)
        for repetition in range(repetitions):
            substring_index = message_letter_by_letter.index(substring)
            message_letter_by_letter[substring_index] = replacement

    instructions = input()

decrypted_message = ''.join(message_letter_by_letter)
print(f'The decrypted message is: {decrypted_message}')
