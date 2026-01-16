result = ''

while True:

    result = ''
    string = input()
    if string == "End":
        break

    if string != 'SoftUni':
        for char in string:
            new_string = char * 2
            result += new_string

        print(result)