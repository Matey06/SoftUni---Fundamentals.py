while True:

    name = input()
    if name == 'Welcome!':
        print('Welcome to Hogwarts.')
        break

    if name == 'Voldemort':
        print('You must not speak of that name!')
        break

    char_num = len(name)

    if char_num < 5:
        print(f'{name} goes to Gryffindor.')
    elif char_num == 5:
        print(f'{name} goes to Slytherin.')
    elif char_num == 6:
        print(f'{name} goes to Ravenclaw.')
    elif char_num > 6:
        print(f'{name} goes to Hufflepuff.')