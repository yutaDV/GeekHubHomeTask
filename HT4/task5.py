'''TASK # 5.   Ну і традиційно - калькулятор: Повинна
бути 1 функцiя, яка приймає 3 аргументи - один з яких операцiя,
яку зробити! Аргументи брати від юзера (можна по одному - окремо 2,
окремо +, окремо 2; можна всі разом - типу 2 + 2).
Операції що мають бути присутні: +, -, *, /, %, //, **.
Не забудьте протестувати з різними значеннями на предмет помилок!'''


def calculator():
    '''Calculator'''

    operators = '+-**//%'
    while True:
        try:
            number_1 = float(input("Input the  first number:  "))
            operator = input("Input operator: ")
            number_2 = float(input("Input the second number:  "))
        except ValueError:
            print('Oops!!! This is not a number. Try again...')
        else:
            if operator in operators:
                if operator in '//%' and number_2 == 0:
                    print('There is not result. Do not / zero!!!Try again.')
                else:
                    break
            else:
                print('NOT a valid optrator, input : +, -, *, /, %, //, **:')
    results = {
        '+': number_1 + number_2, '-': number_1 - number_2,
        '*': number_1 * number_2, '/': number_1 / number_2,
        '%': number_1 % number_2, '//': number_1 // number_2,
        '**': number_1 ** number_2
    }
    for key, value in results.items():
        if key == operator:
            return f'{number_1} {operator} {number_2} = {value}'


print(calculator())
