events = input().split('|')

energy = 100
coins = 100

bakery_status_closed = False

for current_event in events:

    event, number = current_event.split('-')
    number = int(number)

    if event == 'rest':
        if energy + number > 100:
            gained_energy = 100 - energy
            energy = 100
            print(f"You gained {gained_energy} energy.")
        else:
            energy += number
            print(f"You gained {number} energy.")
        print(f"Current energy: {energy}.")
    elif event == 'order':
        if energy >= 30:
            energy -= 30
            coins += number
            print(f"You earned {number} coins.")
        else:
            energy += 50
            print("You had to rest!")
    else:
        if coins >= number:
            coins -= number
            print(f"You bought {event}.")
        else:
            bakery_status_closed = True
            break

if bakery_status_closed:
    print(f"Closed! Cannot afford {event}.")
else:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")