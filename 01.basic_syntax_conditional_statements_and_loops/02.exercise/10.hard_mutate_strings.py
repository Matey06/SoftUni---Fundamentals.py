string1 = input()
string2 = input()

new_string = ''

for i in range(len(string1)):
    if string2[i] != string1[i]:
        new_string = string2[:i + 1] + string1[i + 1:]
        print(string2[:i + 1] + string1[i + 1:])

    if new_string == string2:
        break
