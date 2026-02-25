elements = input().split()
my_dict = {}

for element in elements:
    element = element.lower()
    if element not in my_dict:
        my_dict[element] = 1
    else:
        my_dict[element] += 1

filtered_elements = []

for key, value in my_dict.items():
    if value % 2 != 0:
        filtered_elements.append(key)

print(' '.join(filtered_elements))
