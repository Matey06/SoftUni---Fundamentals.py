import re

furnitures = []
total_price = 0

item = input()

pattern = r'>>([a-z]+)<<([0-9]+\.?[0-9]+)!([0-9]+)'

while item != 'Purchase':

    match = re.search(pattern, item, re.IGNORECASE)

    if match:
        furniture = match.group(1)
        price = match.group(2)
        quantity = match.group(3)

        furnitures.append(furniture)
        total_price += float(price) * int(quantity)

    item = input()


print(f'Bought furniture:')
for current_furniture in furnitures:
    print(current_furniture)
print(f'Total money spend: {total_price:.2f}')
