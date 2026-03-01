courses = {}

while True:

    course_name = input()
    if course_name == 'end':
        break

    name, student = course_name.split(' : ')

    if name not in courses:
        courses[name] = [1, student]
    else:
        courses[name][0] += 1
        courses[name].append(student)

for key, value in courses.items():
    print(f"{key}: {value[0]}")
    for current_student in range(value[0]):
        current_name = value[current_student + 1]
        print(f"-- {current_name}")
