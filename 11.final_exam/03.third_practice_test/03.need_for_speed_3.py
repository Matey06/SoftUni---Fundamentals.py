obtainable_cars = int(input())

cars_and_stats = {}

for current_car in range(obtainable_cars):
    car, mileage, car_fuel = input().split('|')
    mileage = int(mileage)
    car_fuel = int(car_fuel)
    if car not in cars_and_stats:
        cars_and_stats[car] = []
    cars_and_stats[car].append(mileage)
    cars_and_stats[car].append(car_fuel)

command = input()
while command != 'Stop':

    if 'Drive' in command:
        _, car_brand, distance, needed_fuel = command.split(' : ')
        distance = int(distance)
        needed_fuel = int(needed_fuel)
        if car_brand in cars_and_stats:
            if cars_and_stats[car_brand][1] < needed_fuel:
                print('Not enough fuel to make that ride')
            else:
                cars_and_stats[car_brand][0] += distance
                cars_and_stats[car_brand][1] -= needed_fuel
                print(f'{car_brand} driven for {distance} kilometers. {needed_fuel} liters of fuel consumed.')
                if cars_and_stats[car_brand][0] >= 100000:
                    del cars_and_stats[car_brand]
                    print(f'Time to sell the {car_brand}!')

    elif 'Refuel' in command:
        _, car_brand, fuel = command.split(' : ')
        fuel = int(fuel)
        if car_brand in cars_and_stats:
            if cars_and_stats[car_brand][1] + fuel <= 75:
                cars_and_stats[car_brand][1] += fuel
                print(f'{car_brand} refueled with {fuel} liters')
            else:
                refiled_fuel = 75 - cars_and_stats[car_brand][1]
                cars_and_stats[car_brand][1] = 75
                print(f'{car_brand} refueled with {refiled_fuel} liters')


    elif 'Revert' in command:
        _, car_brand, kilometers = command.split(' : ')
        kilometers = int(kilometers)
        if car_brand in cars_and_stats:
            cars_and_stats[car_brand][0] -= kilometers
            if cars_and_stats[car_brand][0] < 10000:
                cars_and_stats[car_brand][0] = 10000
            else:
                print(f'{car_brand} mileage decreased by {kilometers} kilometers')

    command = input()

for key, value in cars_and_stats.items():
    print(f'{key} -> Mileage: {value[0]} kms, Fuel in the tank: {value[1]} lt.')
