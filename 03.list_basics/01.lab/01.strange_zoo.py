animal = []

for _ in range(3):

    animal_part = input()

    animal.append(animal_part)

animal[0], animal[2] = animal[2], animal[0]

print(animal)