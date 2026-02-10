secret_message = input().split()

index = 0

for word in secret_message:

    number = ''
    text = ''
    new_word = ''

    for letter in word:

        if letter.isdigit():
            number += letter
        else:
            text += letter
    new_letter = chr(int(number))
    new_word += new_letter
    new_word += text
    secret_message[index] = new_word
    index += 1

index_ = 0
for word in secret_message:

    current_word = list(word)
    current_word[1], current_word[-1] = current_word[-1], current_word[1]
    secret_message[index_] = ''.join(current_word)
    index_ += 1

print(' '.join(secret_message))