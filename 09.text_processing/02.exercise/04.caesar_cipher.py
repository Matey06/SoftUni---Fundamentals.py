message = input()

ciphertext = ''

for char in message:
    ciphertext += chr(ord(char) + 3)

print(ciphertext)
