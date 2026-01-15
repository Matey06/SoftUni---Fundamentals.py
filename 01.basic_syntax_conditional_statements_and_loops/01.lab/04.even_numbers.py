n = int(input())

count = 0

for _ in range(n):

    count += 1
    number = int(input())

    if number % 2 == 0:
        if count == n:
            print("All numbers are even.")
            break
        continue
    else:
        print(f"{number} is odd!")
        break