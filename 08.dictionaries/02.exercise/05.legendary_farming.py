legendary_items = {'Shadowmourne': {'shards': 0}, 'Valanyr': {'fragments': 0}, 'Dragonwrath': {'motes': 0}}
trash = {}

break_condition = False

while True:

    materials = input().split()

    for current_material in range(0, len(materials), 2):
        quantity = int(materials[current_material])
        material = materials[current_material + 1].lower()

        if material == 'shards':
            legendary_items['Shadowmourne'][material] += quantity
            if legendary_items['Shadowmourne'][material] >= 250:
                print("Shadowmourne obtained!")
                legendary_items['Shadowmourne'][material] -= 250
                break_condition = True
                break

        elif material == 'fragments':
            legendary_items['Valanyr'][material] += quantity
            if legendary_items['Valanyr'][material] >= 250:
                print("Valanyr obtained!")
                legendary_items['Valanyr'][material] -= 250
                break_condition = True
                break

        elif material == 'motes':
            legendary_items['Dragonwrath'][material] += quantity
            if legendary_items['Dragonwrath'][material] >= 250:
                print("Dragonwrath obtained!")
                legendary_items['Dragonwrath'][material] -= 250
                break_condition = True
                break

        else:
            if material not in trash:
                trash[material] = quantity
            else:
                trash[material] += quantity

    if break_condition:
        break

for key, value in legendary_items.items():
    for key2, value2 in value.items():
        print(f"{key2}: {value2}")

for key, value in trash.items():
    print(f"{key}: {value}")
