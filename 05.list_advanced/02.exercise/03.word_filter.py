text = input().split()
filtered = [current for current in text if len(current) % 2 == 0]
for element in filtered:
    print(element)