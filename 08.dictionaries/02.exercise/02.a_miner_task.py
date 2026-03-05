mineral = input()

ores = {}

while mineral != 'stop':
    
    quantity = int(input())

    if mineral not in ores:
        ores[mineral] = quantity
    else:
        ores[mineral] += quantity

    mineral = input()

for mineral, quantity in ores.items():
    print(f'{mineral} -> {quantity}')
