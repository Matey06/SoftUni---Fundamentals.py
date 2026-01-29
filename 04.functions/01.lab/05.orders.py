def coffee_shop_prices(item, quantity):
    """
    water = 1
    coffee = 1.5
    coke = 1.4
    snacks = 2.00
    """
    if item == 'water':
        price = 1 * quantity
        return price
    elif item == 'coffee':
        price = 1.5 * quantity
        return price
    elif item == 'coke':
        price = 1.4 * quantity
        return price
    elif item == 'snacks':
        price = 2.00 * quantity
        return price


item_ = input()
quantity_ = int(input())
result = coffee_shop_prices(item_, quantity_)

print(f'{result:.2f}')