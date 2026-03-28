command = input()

zoo = {}

areas = {}

while command != 'EndDay':

    if 'Add' in command:
        action, details = command.split(' ')
        animal_name, needed_food_quantity, area = details.split('-')
        needed_food_quantity = int(needed_food_quantity)

        if animal_name not in zoo:
            zoo[animal_name] = []
            zoo[animal_name].append(needed_food_quantity)
            zoo[animal_name].append(area)
            if area not in areas:
                areas[area] = []
            areas[area].append(animal_name)
        else:
            zoo[animal_name][0] += needed_food_quantity


    elif 'Feed' in command:
        action, details = command.split(' ')
        current_animal, food = details.split('-')
        food = int(food)
        if current_animal in zoo:
            zoo[current_animal][0] -= food
            if zoo[current_animal][0] <= 0:
                decreasing_area = ''
                for key1, value1 in zoo.items():
                    if key1 == current_animal:
                        decreasing_area = value1[1]
                for key, value in areas.items():
                    if current_animal in value:
                        areas[decreasing_area].remove(current_animal)
                if not areas[decreasing_area]:
                    del areas[decreasing_area]
                del zoo[current_animal]
                print(f'{current_animal} was successfully fed')

    command = input()
print('Animals:')
for animal, stats in zoo.items():
    print(f' {animal} -> {stats[0]}g')

print('Areas with hungry animals:')
for area, animals in areas.items():
    print(f' {area}: {len(animals)}')
