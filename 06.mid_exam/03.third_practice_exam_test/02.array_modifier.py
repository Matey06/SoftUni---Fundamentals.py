numbers = [int(num) for num in input().split()]

command = input()
while command != "end":

    command = command.split()

    if command[0] == 'swap':
        index1 = int(command[1])
        index2 = int(command[2])
        numbers[index1], numbers[index2] = numbers[index2], numbers[index1]

    elif command[0] == 'multiply':
        index1 = int(command[1])
        index2 = int(command[2])
        new_element = numbers[index1] * numbers[index2]
        numbers[index1] = new_element

    elif command[0] == 'decrease':
        for number in range(len(numbers)):
            new_number = numbers[number] - 1
            numbers[number] = new_number

    command = input()

print(*numbers, sep=', ')