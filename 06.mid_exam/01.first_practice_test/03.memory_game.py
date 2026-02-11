elements = input().split()

number_of_moves = 0

while True:

    command = input()

    if command == 'end':
        print(f"Sorry you lose :(")
        print(*elements)
        break

    first_index, second_index = command.split()
    number_of_moves += 1

    first_index = int(first_index)
    second_index = int(second_index)

    if (first_index == second_index or (first_index < 0 or second_index < 0) or
            (first_index >= len(elements) or second_index >= len(elements))):

            half_length = int(len(elements) / 2)
            elements.insert(half_length, f"-{number_of_moves}a")
            elements.insert(half_length + 1, f"-{number_of_moves}a")
            print("Invalid input! Adding additional elements to the board")

    elif elements[first_index] == elements[second_index]:

        popped_element = elements.pop(first_index)
        elements.remove(popped_element)
        print(f"Congrats! You have found matching elements - {popped_element}!")

    elif elements[first_index] != elements[second_index]:

        print("Try again!")

    if not elements:
        print(f"You have won in {number_of_moves} turns!")
        break