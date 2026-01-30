def characters_in_range(char1, char2):
    characters_lst = []
    for character in range(ord(character1), ord(character2) + 1):
        characters_lst.append(chr(character))

    result = (' '.join(characters_lst[1:-1]))

    return result


character1 = input()
character2 = input()
result_ = characters_in_range(character1, character2)

print(result_)