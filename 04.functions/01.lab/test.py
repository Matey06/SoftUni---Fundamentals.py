def sum_numbers(num1: int, num2: int) -> int:

    return num1 + num2

for _ in range(5):

    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    print(sum_numbers(num1, num2))