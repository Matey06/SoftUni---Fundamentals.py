divisor = int(input())
boundery = int(input())

for number in range(boundery, 2, -1):

    if number % divisor == 0:
        print(number)
        break