target = input()

target_cities = {}

while target != 'Sail':
    city, population, gold = target.split('||')
    population = int(population)
    gold = int(gold)
    if city not in target_cities:
        target_cities[city] = [gold, population]
    else:
        target_cities[city][0] += gold
        target_cities[city][1] += population

    target = input()

while True:
    event = input().split('=>')
    if event[0] == 'End':
        break

    elif event[0] == 'Plunder':
        town = event[1]
        people = event[2]
        stolen_gold = event[3]
        people = int(people)
        stolen_gold = int(stolen_gold)
        if town in target_cities:
            print(f'{town} plundered! {stolen_gold} gold stolen, {people} citizens killed.')
            target_cities[town][0] -= stolen_gold
            target_cities[town][1] -= people
            if target_cities[town][0] == 0 or target_cities[town][1] == 0:
                del target_cities[town]
                print(f'{town} has been wiped off the map!')

    elif event[0] == 'Prosper':
        town = event[1]
        added_gold = event[2]
        added_gold = int(added_gold)
        if town in target_cities:
            if added_gold < 0:
                print(f'Gold added cannot be a negative number!')

            else:
                target_cities[town][0] += added_gold
                current_gold = target_cities[town][0]
                print(f'{added_gold} gold added to the city treasury. {town} now has {current_gold} gold.')

if target_cities:
    print(f'Ahoy, Captain! There are {len(target_cities)} wealthy settlements to go to:')
    for current_city, values in target_cities.items():
        print(f'{current_city} -> Population: {values[1]} citizens, Gold: {values[0]} kg')

else:
    print(f'Ahoy, Captain! All targets have been plundered and destroyed!')
