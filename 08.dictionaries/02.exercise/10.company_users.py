employees = {}

info = input()

while info != 'End':

    name, number = info.split(' -> ')

    if name not in employees:
        employees[name] = [number]
    else:
        if number not in employees[name]:
            employees[name].append(number)

    info = input()

for name, numbers in employees.items():
    print(f'{name}')
    for current_number in numbers:
        print(f'-- {current_number}')
