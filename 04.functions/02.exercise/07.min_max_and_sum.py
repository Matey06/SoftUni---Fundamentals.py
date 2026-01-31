numbers = input().split()
integers = [int(number) for number in numbers]

smallest_num = min(integers)
largest_num = max(integers)
summarized_nums = sum(integers)

print(f"The minimum number is {smallest_num}")
print(f"The maximum number is {largest_num}")
print(f"The sum number is: {summarized_nums}")