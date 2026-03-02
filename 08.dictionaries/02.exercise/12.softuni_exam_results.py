exam_results = {}
submissions = {}

while True:

    student = input()
    if student == 'exam finished':
        break

    if 'banned' in student:
        name, ban = student.split('-')
        if name in exam_results:
            exam_results.pop(name)
        continue

    name, language, points = student.split('-')
    points = int(points)

    if name not in exam_results:
        exam_results[name] = [language, points]
        if language not in submissions:
            submissions[language] = 1
        else:
            submissions[language] += 1
    else:
        if points > exam_results[name][1]:
            exam_results[name][1] = points
            submissions[language] += 1
        else:
            submissions[language] += 1


print('Results:')

for key, value in exam_results.items():
    print(f'{key} | {value[1]}')

print('Submissions:')

for key, value in submissions.items():
    print(f'{key} - {value}')