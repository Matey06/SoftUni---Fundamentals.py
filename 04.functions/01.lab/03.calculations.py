def addition(a, b):
    return a + b


def subtraction(a, b):
    return a - b


def multiplication(a, b):
    return a * b


def division(a, b):
    return int(a / b)


def calculator(operator: str, num1: int, num2: int):
    if operator == 'add':
        return addition(num1, num2)
    elif operator == 'subtract':
        return subtraction(num1, num2)
    elif operator == 'multiply':
        return multiplication(num1, num2)
    elif operator == 'divide':
        return division(num1, num2)
    return None


operator_ = input()
num1_ = int(input())
num2_ = int(input())

result = calculator(operator_, num1_, num2_)
print(result)