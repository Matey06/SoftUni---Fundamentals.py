strings_number = int(input())
word = input()

lst = []

for _ in range(strings_number):

    string = input()
    lst.append(string)

print(lst)

filtered_lst = []

for element in lst:

    if word in element:
        filtered_lst.append(element)

print(filtered_lst)