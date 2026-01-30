def smallest_of_three_numbers(num1, num2, num3):
    number_lst = [num1, num2, num3]
    smallest = min(number_lst)
    return smallest


num1_ = int(input())
num2_ = int(input())
num3_ = int(input())
result = smallest_of_three_numbers(num1_, num2_, num3_)
print(result)