'''TASK #  1. Написати функцію <square>, яка прийматиме один аргумент -
сторону квадрата, і вертатиме 3 значення у вигляді кортежа: периметр квадрата,
 площа квадрата та його діагональ.'''


def square(side):
    '''The function calculates the perimeter, area and diagonal of a square'''

    perimeter = 4 * side
    area = side * side
    diagonal = 2 ** 0.5 * side
    result = (perimeter, area, diagonal)
    return result


while True:
    try:
        side = float(input("Input the side of a square:  "))
    except ValueError:
        print('This is invalid value. Goodbye!! Or try again')
    else:
        print(square(side))
        break
