number_of_plants = int(input())

plants_book = {}

for current_plant in range(number_of_plants):
    information = input().split('<->')
    plant_name = information[0]
    plant_rarity = information[1]

    if plant_name not in plants_book:
        plants_book[plant_name] = []
    plants_book[plant_name].append(plant_rarity)

command = input()

while command != 'Exhibition':

    if 'Rate:' in command:
        command = command.split(' ')
        plant_name = command[1]
        rating = int(command[3])
        if plant_name not in plants_book:
            print('error')
        else:
            plants_book[plant_name].append(rating)

    elif 'Update:' in command:
        command = command.split(' ')
        plant_name = command[1]
        new_rarity = command[3]
        if plant_name not in plants_book:
            print('error')
        else:
            plants_book[plant_name][0] = new_rarity

    elif 'Reset:' in command:
        command = command.split(' ')
        plant_name = command[1]
        if plant_name not in plants_book:
            print('error')
        else:
            for _ in range(len(plants_book[plant_name]) - 1):
                plants_book[plant_name].pop()

    command = input()

print('Plants for the exhibition:')
for key, value in plants_book.items():
    number_of_ratings = len(value) - 1
    total_ratings = 0

    for rating in value:
        if type(rating) == str:
            continue
        total_ratings += int(rating)
    if number_of_ratings != 0:
        average_rating = total_ratings / number_of_ratings
    else:
        average_rating = 0
    print(f'- {key}; Rarity: {value[0]}; Rating: {average_rating:.2f}')
