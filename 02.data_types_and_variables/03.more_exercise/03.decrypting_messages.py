key = int(input())
number_of_letters = int(input())

secret_message = ''

for _ in range(number_of_letters):

    letter = input()

    new_letter = (ord(letter) + key)

    secret_message += chr(new_letter)

print(secret_message)