def loading_bar(number):
    first_digit = []
    bar = []

    for digit in str(number):
        first_digit.append(int(digit))
        break

    number = 0

    for index in first_digit:
        number += index

    for percentage in range(number):
        bar.append('%')

    for dots in range(10 - len(bar)):
        bar.append('.')

    return bar

number_ = int(input())
result_ = loading_bar(number_)

if number_ == 100:
    print(f'{number_}% Complete!')
    print(f"[%%%%%%%%%%]")
else:
    print(f"{number_}% [{''.join(result_)}]\nStill loading...")