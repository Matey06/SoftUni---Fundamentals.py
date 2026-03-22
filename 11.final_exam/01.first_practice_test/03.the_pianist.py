number_of_pieces = int(input())

collection_of_pieces = {}

for _ in range(number_of_pieces):
    piece, composer, key = input().split('|')
    if piece not in collection_of_pieces:
        collection_of_pieces[piece] = [composer, key]

command = input()

while command != 'Stop':

    if 'Add' in command:
        _, piece, composer, key = command.split('|')
        if piece not in collection_of_pieces:
            collection_of_pieces[piece] = [composer, key]
            print(f'{piece} by {composer} in {key} added to the collection!')
        else:
            print(f'{piece} is already in the collection!')

    elif 'Remove' in command:
        _, piece = command.split('|')
        if piece in collection_of_pieces:
            del collection_of_pieces[piece]
            print(f'Successfully removed {piece}!')
        else:
            print(f'Invalid operation! {piece} does not exist in the collection.')


    elif 'ChangeKey' in command:
        _, piece, new_key = command.split('|')
        if piece in collection_of_pieces:
            collection_of_pieces[piece][1] = new_key
            print(f'Changed the key of {piece} to {new_key}!')
        else:
            print(f'Invalid operation! {piece} does not exist in the collection.')

    command = input()

for key, value in collection_of_pieces.items():
    print(f'{key} -> Composer: {value[0]}, Key: {value[1]}')
