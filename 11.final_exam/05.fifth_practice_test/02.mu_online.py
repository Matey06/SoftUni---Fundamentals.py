initial_health = 100
initial_bitcoin = 0

all_dungeon_rooms = input().split('|')
best_room = 0

for room in all_dungeon_rooms:
    command, value = room.split()
    best_room += 1

    if command == "potion":
        healing = int(value)
        if healing + initial_health > 100:
            print(f'You healed for {100 - initial_health} hp.')
            initial_health = 100
        else:
            initial_health += healing
            print(f'You healed for {healing} hp.')

        print(f'Current health: {initial_health} hp.')

    elif command == "chest":
        bitcoin = int(value)
        initial_bitcoin += bitcoin
        print(f'You found {bitcoin} bitcoins.')

    else:
        monster = command
        attack = int(value)
        initial_health -= attack

        if initial_health <= 0:
            print(f'You died! Killed by {monster}.\nBest room: {best_room}')
            break
        else:
            print(f'You slayed {monster}.')

if initial_health > 0:
    print(f"You've made it!\nBitcoins: {initial_bitcoin}\nHealth: {initial_health}")
