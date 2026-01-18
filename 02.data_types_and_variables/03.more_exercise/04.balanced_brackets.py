number_of_lines = int(input())

balance = False
first_bracket = False
break_condition = False

for _ in range(number_of_lines):

    random_string = input()

    if random_string == "(" and first_bracket == False:
        balance = True
        first_bracket = True
        continue
    if random_string == "(" and first_bracket == True:
        print("UNBALANCED")
        break

    if random_string == ")":
        first_bracket = False
        if balance:
            balance = False
            continue
        else:
            print("UNBALANCED")
            break_condition = True
            break

if balance != True and break_condition == False:
    print("BALANCED")