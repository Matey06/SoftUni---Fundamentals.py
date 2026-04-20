items = input().split(', ')

while True:
    command = input()
    if command == 'Craft!':
        print(', '.join(items))
        break

    elif 'Collect' in command:
        _, item = command.split(' - ')
        if item not in items:
            items.append(item)

    elif 'Drop' in command:
        _, item = command.split(' - ')
        if item in items:
            items.remove(item)

    elif 'Combine Items' in command:
        _, two_items = command.split(' - ')
        old_item, new_item = two_items.split(':')
        if old_item in items:
            old_item_index = items.index(old_item)
            items.insert(old_item_index + 1, new_item)

    elif 'Renew' in command:
        _, item = command.split(' - ')
        if item in items:
            items.remove(item)
            items.append(item)
