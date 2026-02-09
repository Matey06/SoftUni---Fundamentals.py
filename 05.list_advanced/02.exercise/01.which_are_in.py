first_sequence = input().split(', ')
second_sequence = input().split(', ')
sequence = [first for first in first_sequence if any(first in second for second in second_sequence)]
print(sequence)

#first_sequence = input().split(', ')
#second_sequence = input().split(', ')
#sequence = []

#for first in first_sequence:
    #for second in second_sequence:
        #if first in second:
            #sequence.append(first)
            #break

#print(sequence)