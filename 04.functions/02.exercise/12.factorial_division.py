def factorial_numbers(num1, num2):
    factorial1 = 1
    for num1_factorial in range(1, num1_ + 1):
        factorial1 *= num1_factorial

    factorial2 = 1
    for num2_factorial in range(1, num2_ + 1):
        factorial2 *= num2_factorial

    return calculations(factorial1, factorial2)

def calculations(factorial1, factorial2):
    result = factorial1 / factorial2
    return result


num1_ = int(input())
num2_ = int(input())
result_ = factorial_numbers(num1_, num2_)
print(f'{result_:.2f}')