cars = int(input())

parking_lot = {}

for car in range(cars):

    info = input().split()

    if info[0] == 'register':
        name = info[1]
        plate_number = info[2]
        if name not in parking_lot:
            parking_lot[name] = plate_number
            print(f"{name} registered {plate_number} successfully")
        else:
            print(f"ERROR: already registered with plate number {plate_number}")

    elif info[0] == 'unregister':
        name = info[1]
        if name not in parking_lot:
            print(f"ERROR: user {name} not found")
        else:
            parking_lot.pop(name)
            print(f"{name} unregistered successfully")

for key, value in parking_lot.items():
    print(f"{key} => {value}")
