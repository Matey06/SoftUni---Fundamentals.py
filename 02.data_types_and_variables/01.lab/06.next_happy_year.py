year = int(input())

while True:
    year += 1
    new_year = str(year)

    if len(new_year) == len(set(new_year)):
        break

print(year)