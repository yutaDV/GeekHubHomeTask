'''TASK # 3.  Користувач вводить змінні "x" та "y" з довільними цифровими
значеннями. Створіть просту умовну конструкцію (звiсно вона повинна бути
в тiлi ф-цiї), під час виконання якої буде перевірятися рівність змінних
"x" та "y" та у випадку нерівності - виводити ще і різницю.
Повинні працювати такі умови (x, y, z заміність на відповідні числа):
    x > y;       вiдповiдь - "х бiльше нiж у на z"
    x < y;       вiдповiдь - "у бiльше нiж х на z"
    x == y.      відповідь - "х дорівнює y".'''


def comparing_numbers(number_1, number_2):
    '''Function is comparing two numbers.'''
    if number_1 > number_2:
        return f'{number_1} is more than {number_2} to {number_1 - number_2}'
    elif number_1 < number_2:
        return f'{number_2} is more than {number_1} to {number_2 - number_1}'
    else:
        return f'{number_2} equals {number_1}'


while True:
    try:
        x = float(input("Please, input a  number x:  "))
        y = float(input("Input a number y:  "))
        break
    except ValueError:
        print('You nead to input numbers. Try again...')
print(comparing_numbers(x, y))
