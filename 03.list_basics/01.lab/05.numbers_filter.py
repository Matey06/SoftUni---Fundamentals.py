integers_number = int(input())

lst = []

for _ in range(integers_number):

    number = int(input())

    lst.append(number)

statement = input()
filtered_lst = []

for element in lst:
    if statement == 'even':
        if element % 2 == 0 or element == 0:
            filtered_lst.append(element)
    elif statement == 'odd':
        if element % 2 != 0:
            filtered_lst.append(element)
    elif statement == 'positive':
        if element >= 0:
            filtered_lst.append(element)
    elif statement == 'negative':
        if element < 0:
            filtered_lst.append(element)

print(filtered_lst)