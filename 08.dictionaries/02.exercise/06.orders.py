catalogue = {}

while True:

    product = input()
    if product == "buy":
        break

    item, price, quantity = product.split()
    price = float(price)
    quantity = int(quantity)

    if item not in catalogue:
        catalogue[item] = [price, quantity]
    else:
        catalogue[item][0] = price
        catalogue[item][1] += quantity

for key, value in catalogue.items():
    total_price = value[0] * value[1]
    print(f"{key} -> {total_price:.2f}")
