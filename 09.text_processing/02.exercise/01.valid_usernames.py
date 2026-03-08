usernames = input().split(', ')

for name in usernames:

    valid_name = False

    for char in name:

        if 3 <= len(name) <= 16:
            valid_name = True

        if not char.isalnum() and char != '_' and char != '-' :
            valid_name = False
            break

    if valid_name:
        print(name)
