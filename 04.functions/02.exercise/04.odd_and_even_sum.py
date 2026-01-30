def even_odd_sum(number):

    even = []
    odd = []

    for digit in str(number):
        if int(digit) % 2 == 0 or int(digit) == 0:
            even.append(int(digit))
        else:
            odd.append(int(digit))

    even_sum = sum(even)
    odd_sum = sum(odd)
    return even_sum ,odd_sum


number_ = int(input())
even_sum_, odd_sum_ = even_odd_sum(number_)

print(f'Odd sum = {odd_sum_}, Even sum = {even_sum_}')