characters = input().split(', ')
ascii_score = []

for character in characters:
    score = ord(character)
    ascii_score.append(score)

my_dict = {key: value for key, value in zip(characters, ascii_score)} #New method learned(zip)
print(my_dict)


#Second way: -> First solution I came up with
#characters = input().split(', ')
#ascii_score = []

#for character in characters:
    #score = ord(character)
    #ascii_score.append(score)

#my_dict = {}

#for element in range(len(characters)):
    #my_dict[characters[element]] = ascii_score[element]

#print(my_dict)


#Third Way: -> Best Solution
#characters = input().split(', ')
#my_dict = {ch: ord(ch) for ch in characters}
#print(my_dict)