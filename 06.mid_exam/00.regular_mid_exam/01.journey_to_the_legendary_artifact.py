energy = float(input())

pieces = 0
mountains_count = 0

terrain = input()

while terrain != 'Journey ends here!':

    if terrain == 'mountain':
        energy -= 10
        mountains_count += 1
        if mountains_count % 3 == 0:
            pieces += 1
            if pieces == 3:
                print(f'The character reached the legendary artifact with {energy:.2f} energy left.')
                break

    elif terrain == 'desert':
        energy -= 15

    elif terrain == 'forest':
        energy += 7

    if energy <= 0:
        print('The character is too exhausted to carry on with the journey.')
        break

    terrain = input()


if pieces < 3 and energy > 0:
    needed_pieces = 3 - pieces
    print(f'The character could not find all the pieces and needs {needed_pieces} '
          f'more to complete the legendary artifact.')