sorted_list = [0] * 11

while True:

    to_do_notes = input().split('-')

    if to_do_notes[0] == 'End':
        break

    importance, note = to_do_notes

    index = int(importance)
    sorted_list[index] = note

no_zeros = []

for element in sorted_list:
    if element != 0:
        no_zeros.append(element)

print(no_zeros)