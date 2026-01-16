messages_num = int(input())

for i in range (messages_num):

    number = int(input())

    if number == 88:
        print("Hello")
    elif number == 86:
        print("How are you?")
    elif number < 88:
        print("GREAT!")
    else:
        print("Bye.")