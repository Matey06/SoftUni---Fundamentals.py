number_of_pieces = int(input())

collection_of_pieces = {}

for current_piece in range(number_of_pieces):
    piece, composer, key = input().split('|')
    if key not in collection_of_pieces:
        collection_of_pieces[key] = []
    collection_of_pieces[key].append(composer)
    collection_of_pieces[key].append(piece)

command = input()

while command != 'Stop':

    if 'Add' in command:
        _, piece, composer, key = command.split('|')
        if key not in collection_of_pieces:
            collection_of_pieces[key] = []
        if not any(piece in lst for lst in collection_of_pieces.values()):
            collection_of_pieces[key].append(composer)
            collection_of_pieces[key].append(piece)
            print(f'{piece} by {composer} in {key} added to the collection!')
        else:
            print(f'{piece} is already in the collection!')

    elif 'Remove' in command:
        _, piece = command.split('|')
        if any(piece in lst for lst in collection_of_pieces.values()):
            for key, value in collection_of_pieces.items():
                if piece in value:
                    collection_of_pieces[key].remove(piece)
                    print(f'Successfully removed {piece}!')
        else:
            print(f'Invalid operation! {piece} does not exist in the collection.')


    elif 'ChangeKey' in command:
        _, piece, new_key = command.split('|')
        copy = collection_of_pieces.copy()
        if any(piece in lst for lst in collection_of_pieces.values()):
            for key, value in copy.items():
                if piece in value:
                    collection_of_pieces[new_key] = collection_of_pieces.pop(key)
                    print(f'Changed the key of {piece} to {new_key}!')
        else:
            print(f'Invalid operation! {piece} does not exist in the collection.')

    command = input()

for key, values in collection_of_pieces.items():
    index1 = 0
    index2 = 0
    current_piece = ''
    current_composer = ''
    for value in values:
        if index1 == 0:
            current_composer = value
            index1 += 1
        elif index2 == 0:
            current_piece = value
            index2 += 1

        if index1 == 1 and index2 == 1:
            print(f'{current_piece} -> Composer: {current_composer}, Key: {key}')
            index1 = 0
            index2 = 0
