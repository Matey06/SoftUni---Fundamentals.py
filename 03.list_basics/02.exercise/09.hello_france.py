collection_of_items = input().split('|')
budget = float(input())

train_ticket = 150
profit = 0

new_prices = []
new_prices_filtered = []

for item in collection_of_items:

    type_of_item, price = item.split('->')
    price = float(price)

    if type_of_item == 'Clothes':
        if price > 50.00:
            continue
        else:
            if budget >= price:
                budget -= price
            else:
                continue
    elif type_of_item == 'Shoes':
        if price > 35.00:
            continue
        else:
            if budget >= price:
                budget -= price
            else:
                continue
    elif type_of_item == 'Accessories':
        if price > 20.50:
            continue
        else:
            if budget >= price:
                budget -= price
            else:
                continue

    new_prices.append(price)

for current_price in new_prices:

    current_price = float(current_price)

    new_price = current_price * 1.40
    budget += new_price
    profit += new_price - current_price
    new_prices_filtered.append(f'{new_price:.2f}')

print(' '.join(map(str, new_prices_filtered)))
print(f"Profit: {profit:.2f}")
if budget >= train_ticket:
    print("Hello, France!")
else:
    print("Not enough money.")