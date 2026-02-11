groceries = input().split('!')

while True:

    command = input().split()
    if command[0] == 'Go':
        break

    if command[0] == 'Urgent':
        if command[1] not in groceries:
            groceries.insert(0, command[1])
    elif command[0] == 'Unnecessary':
        if command[1] in groceries:
            groceries.remove(command[1])
    elif command[0] == 'Correct':
        if command[1] in groceries:
            index = groceries.index(command[1])
            groceries.insert(index, command[2])
            groceries.pop(index + 1) #groceries.remove(command[1])
    elif command[0] == 'Rearrange':
        if command[1] in groceries:
            groceries.remove(command[1])
            groceries.append(command[1])

print(', '.join(groceries))