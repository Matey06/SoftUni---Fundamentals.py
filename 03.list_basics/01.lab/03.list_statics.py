numbers = int(input())

positive_numbers = []
negative_numbers = []

positive_counter = 0
negative_sum = 0

for _ in range(numbers):

    num = int(input())

    if num > 0:
        positive_numbers.append(num)
        positive_counter += 1
    else:
        negative_numbers.append(num)
        negative_sum += num

print(positive_numbers)
print(negative_numbers)
print(f"Count of positives: {positive_counter}\nSum of negatives: {negative_sum}")