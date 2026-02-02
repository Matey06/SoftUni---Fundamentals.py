def tribonacci_sequence(number):
    sequence = []

    for _ in range(number):
        if len(sequence) == 0:
            sequence.append(1)
        elif len(sequence) == 1:
            sequence.append(1)
        elif len(sequence) == 2:
            sequence.append(2)
        elif len(sequence) >= 3:
            sequence.append(sequence[-1] + sequence[-2] + sequence[-3])

    return sequence


number_ = int(input())
result_ = tribonacci_sequence(number_)
# ways to remove numbers from int list --> lst = [1, 2, 3, 4, 5]
# N1 - print(*lst)
# N2 - print(' '.join(map(str, lst)))
print(' '.join(map(str, result_)))