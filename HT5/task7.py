'''TASK #7 ННаписати функцію, яка приймає на вхід список (через кому),
підраховує кількість однакових елементів у ньому і виводить результат.
Елементами списку можуть бути дані будь-яких типів.
    Наприклад:
    1, 1, 'foo', [1, 2], True, 'foo', 1, [1, 2] ----> 
    "1 -> 3, foo -> 2, [1, 2] -> 2, True -> 1"'''


def doubles():

    while True:
        values = input("Please, type values seperated ONLY by a comma :")
        our_list = values.split(',')
        try:
            shift = int(input("Input a number for shift:  "))
        except ValueError:
            print('This is invalid value. Input a number:')
        else:
            if shift <= len(our_list):
                break
            else:
                print('This is invalid value. Try again:')
    new_list = our_list[-shift:] + our_list[:-shift]
    return new_list


print(doubles())
