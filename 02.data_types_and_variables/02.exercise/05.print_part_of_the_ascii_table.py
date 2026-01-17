start = int(input())
finish = int(input())

for number in range(start, finish + 1):
    if number == finish:
        print(chr(number))
    else:
        print(chr(number), end=' ')