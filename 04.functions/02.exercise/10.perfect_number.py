def perfect_number(number):
    divisors = []
    for digit in range(1, number):
        if number % digit == 0:
            divisors.append(digit)

    if sum(divisors) == number:
        perfect_result = "We have a perfect number!"
        return perfect_result
    else:
        not_perfect_result = "It's not so perfect."
        return not_perfect_result

number_ = int(input())
result = perfect_number(number_)

print(result)