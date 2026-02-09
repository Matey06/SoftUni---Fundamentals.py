current_version = list(map(int, input().split('.')))
next_version3 = current_version[-1] + 1
if next_version3 > 9:
    next_version2 = current_version[-2] + 1
    if next_version2 > 9:
        next_version1 = current_version[-3] + 1
        current_version.insert(-3, next_version1)
        for _ in range(3):
            current_version.pop()
        for _ in range(2):
            current_version.append(0)
    else:
        current_version.insert(-2, next_version2)
        for _ in range(2):
            current_version.pop()
        current_version.append(0)
else:
    current_version.insert(-1, next_version3)
    current_version.pop()

print('.'.join(list(map(str, current_version))))