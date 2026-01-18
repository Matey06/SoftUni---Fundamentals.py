budget = float(input())
price_per_kg_flower = float(input())
price_per_pack_of_eggs = 0.75 * price_per_kg_flower
price_per_liter_of_milk = 1.25 * price_per_kg_flower
price_per_250_ml_of_milk = 0.25 * price_per_liter_of_milk

easter_break_price = price_per_250_ml_of_milk + price_per_pack_of_eggs + price_per_kg_flower

easter_break_counter = 0
colored_eggs_counter = 0

while True:

    if easter_break_price > budget:
        print(f"You made {easter_break_counter} loaves of Easter bread! Now you have "
              f"{colored_eggs_counter} eggs and {budget:.2f}BGN left.")
        break

    budget -= easter_break_price
    easter_break_counter += 1
    colored_eggs_counter += 3

    if easter_break_counter % 3 == 0:
        colored_eggs_counter -= easter_break_counter - 2