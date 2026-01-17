number_of_lines = int(input())

water_tank_capacity = 255 #liters

for i in range(number_of_lines):

    liters_of_water = int(input())

    if liters_of_water > water_tank_capacity:
        print("Insufficient capacity!")
        continue

    water_tank_capacity -= liters_of_water

print(255 - water_tank_capacity)