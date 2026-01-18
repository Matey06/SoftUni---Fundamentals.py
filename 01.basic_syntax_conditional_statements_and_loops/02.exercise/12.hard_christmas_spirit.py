quantity_of_decorations = int(input())
days_until_christmas = int(input())

ornament_set = 2
tree_skirt = 5
tree_garlant = 3
tree_lights = 15

christmas_spirit = 0
money_spend = 0

for i in range(1, days_until_christmas + 1):

    if i % 11 == 0:
        quantity_of_decorations += 2

    if i % 2 == 0:
        money_spend += ornament_set * quantity_of_decorations
        christmas_spirit += 5

    if i % 3 == 0:
        money_spend += (tree_skirt + tree_garlant) * quantity_of_decorations
        christmas_spirit += 10 + 3

    if i % 5 == 0:
        money_spend += tree_lights * quantity_of_decorations
        christmas_spirit += 17
        if i % 3 == 0:
            christmas_spirit += 30

    if i % 10 == 0:
        christmas_spirit -= 20
        money_spend += tree_skirt + tree_garlant + tree_lights

if days_until_christmas % 10 == 0:
    christmas_spirit -= 30

print(f"Total cost: {money_spend}\nTotal spirit: {christmas_spirit}")