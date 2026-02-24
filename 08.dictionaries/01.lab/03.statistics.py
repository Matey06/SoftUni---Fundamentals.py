products = {}

while True:
    command = input()
    if command == "statistics":
        break

    food, quantity = command.split(': ')
    quantity = int(quantity)

    if food not in products:
        products[food] = quantity
    else:
        products[food] += quantity

products_count = len(products)
total_value = sum(products.values())

print("Products in stock:")
for food, quantity in products.items():
    print(f"- {food}: {quantity}")
print(f"Total Products: {products_count}")
print(f"Total Quantity: {total_value}")
