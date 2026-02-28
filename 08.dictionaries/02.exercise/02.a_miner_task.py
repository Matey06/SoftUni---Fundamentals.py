line_number = 0

mineral = input()

ores = {}

while mineral != 'stop':
    line_number += 1

    quantity = int(input())

    if mineral not in ores:
        ores[mineral] = quantity
    else:
        ores[mineral] += quantity

    mineral = input()

for mineral, quantity in ores.items():
    print(f'{mineral} -> {quantity}')
