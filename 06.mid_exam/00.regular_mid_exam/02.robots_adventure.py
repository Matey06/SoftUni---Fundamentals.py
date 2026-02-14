items = [int(num) for num in input().split('|')]

collected_items = 0

command = input()

while command != 'Adventure over':

    if 'Backward' in command:
        command = command.split('$')
        first_number = int(command[1])
        second_number = int(command[2])
        if 0 <= first_number < len(items):
            chosen = (first_number - second_number) % len(items)
            collected_items += items[chosen]
            items[chosen] = 0

    elif 'Forward' in command:
        command = command.split('$')
        first_number = int(command[1])
        second_number = int(command[2])
        if 0 <= first_number < len(items):
            chosen = (first_number + second_number) % len(items)
            collected_items += items[chosen]
            items[chosen] = 0

    elif 'Double' in command:
        command = command.split()
        number = int(command[1])
        if 0 <= number < len(items):
            current_item = items[number]
            current_item *= 2
            items[number] = current_item

    elif command == 'Switch':
        items.reverse()

    command = input()

print(*items, sep=' - ')
print(f'Robo finished the adventure with {collected_items} items!')