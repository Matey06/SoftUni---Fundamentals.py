phonebook = {}

while True:

    entry = input()
    if '-' not in entry:
        break
    else:
        name, number = entry.split('-')

    phonebook[name] = number

entry = int(entry)

for _ in range(entry):

    name = input()

    if name in phonebook:
        print(f'{name} -> {phonebook[name]}')
    else:
        print(f'Contact {name} does not exist.')
