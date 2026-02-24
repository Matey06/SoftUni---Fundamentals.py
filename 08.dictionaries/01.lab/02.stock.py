data = input().split()

my_dict = {}
for item in range(0, len(data), 2):
    food = data[item]
    quantity = int(data[item + 1])
    my_dict[food] = quantity

products = input().split()

for product in products:
    if product in my_dict:
        print(f"We have {my_dict[product]} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")
