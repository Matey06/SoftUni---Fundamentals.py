electrons_number = int(input())

shells_lst = []

current_shell = 1

while electrons_number > 0:

    shell = 2 * (current_shell ** 2)
    if electrons_number > shell:
        shells_lst.append(shell)
    else:
        shells_lst.append(electrons_number)
        electrons_number = 0
    electrons_number -= shell

    current_shell += 1

print(shells_lst)