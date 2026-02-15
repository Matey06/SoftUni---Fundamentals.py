targets = [int(num) for num in input().split()]

command = input()

shot_targets = 0

while command != "End":

    index = int(command)

    if 0 <= index < len(targets):
        shot_targets += 1
        value = targets[index]
        targets[index] = -1
        for current_target in range(len(targets)):
            if targets[current_target] != -1 and targets[current_target] <= value:
                targets[current_target] += value
            elif targets[current_target] != -1 and targets[current_target] > value:
                targets[current_target] -= value

    command = input()

unpacked_values = ' '.join(map(str, targets))
print(f'Shot targets: {shot_targets} -> {unpacked_values}')