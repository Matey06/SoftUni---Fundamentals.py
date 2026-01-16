number_of_orders = int(input())

total = 0

for _ in range(number_of_orders):

    capsule_price = float(input())
    days = int(input())
    capsules_per_day = int(input())

    if not (0.01 <= capsule_price <= 100.00):
        continue

    if not(1 <= days <= 31):
        continue

    if not(1 <= capsules_per_day <= 2000):
        continue

    total_capsules_price = capsule_price * capsules_per_day
    coffe_price = total_capsules_price * days

    total += coffe_price

    print(f"The price for the coffee is: ${coffe_price:.2f}")

print(f"Total: ${total:.2f}")