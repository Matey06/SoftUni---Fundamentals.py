lost_fights_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

total_expenses = 0

broken_shields = 0

for current_loss in range(1, lost_fights_count + 1):

    if current_loss % 2 == 0:
        total_expenses += helmet_price

    if current_loss % 3 == 0:
        total_expenses += sword_price
        if current_loss % 2 == 0:
            total_expenses += shield_price
            broken_shields += 1

    if broken_shields == 2:
        total_expenses += armor_price
        broken_shields = 0

print(f"Gladiator expenses: {total_expenses:.2f} aureus")