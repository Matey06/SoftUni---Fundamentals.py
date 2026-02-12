rooms = input().split('|')

health = 100
bitcoin = 0
room_counter = 0

for room in rooms:

    command, number = room.split()
    number = int(number)
    room_counter += 1

    if command == 'potion':
        if health < 100 and health + number <= 100:
            health += number
            print(f"You healed for {number} hp.")
            print(f"Current health: {health} hp.")
        elif health + number > 100:
            healing_amound = 100 - health
            health = 100
            print(f"You healed for {healing_amound} hp.")
            print(f"Current health: {health} hp.")
    elif command == 'chest':
        bitcoin += number
        print(f"You found {number} bitcoins.")
    else:
        health -= number
        if health > 0:
            print(f"You slayed {command}.")
        else:
            print(f"You died! Killed by {command}.")
            print(f"Best room: {room_counter}")
            break

if health > 0:
    print("You've made it!")
    print(f"Bitcoins: {bitcoin}")
    print(f"Health: {health}")