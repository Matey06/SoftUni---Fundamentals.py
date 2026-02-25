students = {}

while True:

    line = input()
    if ":" not in line:
        course_name = line
        break

    name, data, study = line.split(':')

    if name not in students:
        students[name] = {}

    students[name][int(data)] = study

for outer_key, data in students.items():
    for key, course in data.items():
        formated_course = "_".join(course.split())
        if formated_course == course_name:
            print(f"{outer_key} - {key}")
