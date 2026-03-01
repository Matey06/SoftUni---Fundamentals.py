number_of_students = int(input())

grades_book = {}

for student in range(number_of_students):

    name = input()
    grade = float(input())

    if name not in grades_book:
        grades_book[name] = [grade, 1]
    else:
        grades_book[name][0] += grade
        grades_book[name][1] += 1

for key, value in grades_book.items():
    average_grade = value[0] / value[1]
    if average_grade >= 4.50:
        print(f"{key} -> {average_grade:.2f}")
