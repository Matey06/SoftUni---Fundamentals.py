rooms = int(input())

total_free_chairs = 0
break_condition = False

for current_room in range(1, rooms + 1):

    chairs, visitors = input().split()
    visitors = int(visitors)

    if len(chairs) < visitors:
        needed_chairs = visitors - len(chairs)
        break_condition = True
        print(f'{needed_chairs} more chairs needed in room {current_room}')
    else:
        total_free_chairs += len(chairs) - visitors

if not break_condition:
    print(f'Game On, {total_free_chairs} free chairs left')