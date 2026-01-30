def sum_numbers(num1, num2):
    return num1 + num2


def subtract_numbers(num1, num2, num3):
    result = sum_numbers(num1, num2) - num3
    return result


def calculations(num1, num2, num3):
    return subtract_numbers(num1, num2, num3)


num1_ = int(input())
num2_ = int(input())
num3_ = int(input())

outcome = calculations(num1_, num2_, num3_)

print(outcome)