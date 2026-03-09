text = input()

unique_chars = []

for char in text:

    if len(unique_chars) == 0:
        unique_chars.append(char)

    elif char != unique_chars[-1]:
        unique_chars.append(char)

    else:
        continue

print(''.join(unique_chars))

# Second solution -> easier
#text = input()

#new_text = ""

#for char in text:
    #if new_text == "":
        #new_text += char

    #elif char != new_text[-1]:
        #new_text += char

#print(new_text)