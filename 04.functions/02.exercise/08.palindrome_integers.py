def palindrome_numbers(integers):

    result = []
    for integer in integers:
        integer = str(integer)
        if integer[0] == integer[-1]:
            result.append(True)
        else:
            result.append(False)

    return result

numbers = input().split(', ')
integers_ = [int(number) for number in numbers]
result_ = palindrome_numbers(integers_)
string_result = map(str, result_)
print('\n'.join(string_result))