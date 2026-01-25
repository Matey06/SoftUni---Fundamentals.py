string_of_integers = input().split(', ')
string_of_integers = list(map(int, string_of_integers))
beggars_num = int(input())

profit_lst = []

current_profit = 0

for beggar in range(beggars_num):

    current_profit = 0

    for profit in range(beggar, len(string_of_integers), beggars_num):

        current_profit += string_of_integers[profit]

    profit_lst.append(current_profit)

print(profit_lst)