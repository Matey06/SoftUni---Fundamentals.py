foods_and_quantities = input().split()

my_dict = {}

for element in range(0, len(foods_and_quantities), 2):
    food = foods_and_quantities[element]
    quantity = foods_and_quantities[element + 1]
    my_dict[food] = int(quantity)

print(my_dict)
