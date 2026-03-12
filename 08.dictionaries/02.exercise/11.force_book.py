force_book = {}

command = input()

while command != 'Lumpawaroo':

    already_has_a_side = False

    if ' | ' in command:
        force_side, force_user = command.split(' | ')
        if force_side not in force_book:
            force_book[force_side] = []
        for value in force_book.values():
            if force_user in value:
                already_has_a_side = True
                break
        if not already_has_a_side:
            force_book[force_side].append(force_user)

    elif ' -> ' in command:
        force_user, force_side = command.split(' -> ')
        old_side = None

        for side, users in force_book.items():
            if force_user in users:
                old_side = side
                break

        if old_side:
            force_book[old_side].remove(force_user)

        if force_side not in force_book:
            force_book[force_side] = []

        force_book[force_side].append(force_user)

        print(f"{force_user} joins the {force_side} side!")

    command = input()

for key, values in force_book.items():
    if force_book[key]:
        print(f'Side: {key}, Members: {len(force_book[key])}')
        for value in values:
            print(f'! {value}')
