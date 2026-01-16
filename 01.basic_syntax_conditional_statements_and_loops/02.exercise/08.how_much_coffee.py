coffee_count = 0

while True:

    command = input()
    if command == 'END':
        break

    if (command == 'cat' or command == 'CAT'
            or command == 'dog' or command == 'DOG'
            or command == 'coding' or command == 'CODING'
            or command == 'movie' or command == 'MOVIE'):
        if command == command.lower():
            coffee_count += 1
        elif command == command.upper():
            coffee_count += 2

if coffee_count < 6:
    print(coffee_count)
else:
    print("You need extra sleep")