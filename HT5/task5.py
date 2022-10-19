'''TASK #5 Написати функцію <fibonacci>, яка приймає один аргумент
 і виводить всі числа Фібоначчі, що не перевищують його '''


def fibonacci():

    while True:
        try:
            number = int(input("Input a number:  "))
        except ValueError:
            print('This is invalid value. Input a number:')
        else:
            if number >= 0:
                break
            else:
                print('This is invalid value. Try again:')
    if number == 0:
        return number
    else:
        result = [0, 1]
        for i in range(0, number + 1):
            if i == result[-1] + result[-2]:
                result.append(i)
        return result


print(fibonacci())
