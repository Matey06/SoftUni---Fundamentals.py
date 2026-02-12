pirate_ship = [int(num) for num in input().split('>')]
warship = [int(num) for num in input().split('>')]
maximum_health_capacity = int(input())

while True:

    text = input().split()
    if text[0] == 'Retire':
        print(f"Pirate ship status: {sum(pirate_ship)}")
        print(f"Warship status: {sum(warship)}")
        break

    command = text[0]

    if command == 'Fire':
        index = int(text[1])
        damage = int(text[2])
        if 0 <= index < len(warship):
            section = warship[index]
            section -= damage
            if section <= 0:
                print("You won! The enemy ship has sunken.")
                break
            else:
                warship[index] = section

    elif command == 'Defend':
        break_condition = False
        start_index = int(text[1])
        end_index = int(text[2])
        damage = int(text[3])
        if 0 <= start_index < len(pirate_ship) and 0 <= end_index < len(pirate_ship):
            for current_ship in range(start_index, end_index + 1):
                attacked_ship = pirate_ship[current_ship]
                attacked_ship -= damage
                if attacked_ship <= 0:
                    print("You lost! The pirate ship has sunken.")
                    break_condition = True
                    break
                else:
                    pirate_ship[current_ship] = attacked_ship
        if break_condition:
            break

    elif command == 'Repair':
        index = int(text[1])
        health = int(text[2])
        if 0 <= index < len(pirate_ship):
            section = pirate_ship[index]
            section += health
            if section > maximum_health_capacity:
                section = maximum_health_capacity
                pirate_ship[index] = section
            else:
                pirate_ship[index] = section

    elif command == 'Status':
        needs_repair = 0
        for current_section in pirate_ship:
            if current_section < (maximum_health_capacity * 0.2):
                needs_repair += 1
        print(f"{needs_repair} sections need repair.")