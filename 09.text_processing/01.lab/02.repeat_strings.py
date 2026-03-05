text = input().split()

concatenated_string = ''

for word in text:
    for number in range(len(word)):
        concatenated_string += word

print(concatenated_string)
