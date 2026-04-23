def calculations(list_of_numbers, removed_element_):
    removed_element_ = int(removed_element_)
    for i, number in enumerate(list_of_numbers):
        number = int(number)
        if number <= int(removed_element_):
            numbers[i] = str(number + removed_element_)
        else:
            numbers[i] = str(number - removed_element_)


numbers = input().split()
removed = []

while numbers:
    index = int(input())

    if 0 <= index < len(numbers):
        removed_element = numbers.pop(index)
        removed.append(removed_element)
        calculations(numbers, removed_element)

    elif index < 0:
        removed_element = numbers[0]
        removed.append(removed_element)
        numbers[0] = numbers[-1]
        calculations(numbers, removed_element)

    else:
        removed_element = numbers[-1]
        removed.append(removed_element)
        numbers[-1] = numbers[0]
        calculations(numbers, removed_element)

total_sum = 0

for num in removed:
    total_sum += int(num)

print(total_sum)
