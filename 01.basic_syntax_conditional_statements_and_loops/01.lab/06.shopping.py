budget = int(input())

spent = 0

while True:

    price = input()
    if price == 'End':
        print("You bought everything needed.")
        break

    price = int(price)

    spent += price

    if budget < spent:
        print("You went in overdraft!")
        break