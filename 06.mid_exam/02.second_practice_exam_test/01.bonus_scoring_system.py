from math import ceil

students = int(input())
lectures = int(input())
additional_bonus = int(input())

best_score = 0
best_student_attendance = 0

for current_student in range(students):

    attendance = int(input())

    total_bonus = attendance / lectures * (5 + additional_bonus)
    if total_bonus > best_score:
        best_score = total_bonus
        best_student_attendance = attendance

print(f"Max Bonus: {ceil(best_score)}.")
print(f"The student has attended {best_student_attendance} lectures.")