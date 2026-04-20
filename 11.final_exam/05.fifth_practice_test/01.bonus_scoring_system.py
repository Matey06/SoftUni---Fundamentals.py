from math import ceil

number_of_students = int(input())
number_of_lectures = int(input())
additional_bonus = int(input())

max_bonus = 0
attended_lectures = 0

for current_student in range(number_of_students):
    attendance = int(input())

    current_bonus = attendance / number_of_lectures * (5 + additional_bonus)
    if current_bonus > max_bonus:
        max_bonus = current_bonus
        attended_lectures = attendance

print(f'Max Bonus: {ceil(max_bonus)}.')
print(f'The student has attended {attended_lectures} lectures.')
