targets = [int(num) for num in input().split()]

command = input()

while command != "End":

    action, index, value = command.split()
    index = int(index)
    value = int(value)

    if action == "Shoot":
        if 0 <= index < len(targets):
            targets[index] -= value
            if targets[index] <= 0:
                targets.remove(targets[index])

    elif action == "Add":
        if 0 <= index < len(targets):
            targets.insert(index, value)
        else:
            print('Invalid placement!   ')

    elif action == "Strike":
        if 0 <= index < len(targets):
            target_value = targets[index]
            if 0 <= index - value < len(targets) and 0 <= index + value < len(targets):
                for current in range(value):
                    targets.pop(index - 1)
                    targets.pop(index)
                targets.remove(target_value)
            else:
                print('Strike missed!')

    command = input()

print(*targets, sep='|')