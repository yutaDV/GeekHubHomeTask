'''TASK # 2. Створіть 3 рiзних функцiї (на ваш вибiр). Кожна з цих функцiй
повинна повертати якийсь результат (напр. інпут від юзера, результат
математичної операції тощо). Також створiть четверту ф-цiю,
яка всередині викликає 3 попередні'''


def correct_yers():
    '''Функція перевіряє чи коректно введено рік'''

    while True:
        try:
            year = int(input("Input the  year:  "))
        except ValueError:
            print('Oops!!! This is not a number. Try again...')
        else:
            if year > 0:
                return year
            else:
                print('Oops! This number is not greater than zero. Try again.')


def years(year):
    '''Функція перевіряє чи є рік високосним'''

    if year % 400 == 0:
        return True
    else:
        if year % 4 == 0 and year % 100 != 0:
            return True


def correct_month():
    ''' Функція перевіряє чи коректно вказано номер місяця'''

    while True:
        try:
            month = int(input("Input a month number:  "))
        except ValueError:
            print('You nead to input a number from 1 to 12. Try again...')
        else:
            if month in range(1, 13):
                return month
            else:
                print('This number is not from 1 to 12. Try again...')


def days_in_month(month):
    '''Функція приймає місяця та повертає кількіст днів у даному місяці'''

    days = {
        '31 days': [1, 3, 5, 7, 8, 10, 12],
        '28 days or 29': [2],
        '30 days': [4, 6, 9, 11]
    }
    for key, value in days.items():
        if month in value:
            return key


def correct_data():
    '''Функція перевіря чи введена дата є реальною'''

    print('Please! Enter the date in the format YYYY.MM.DD')
    year = correct_yers()
    month = correct_month()
    while True:
        try:
            day = int(input("Input a day:  "))
        except ValueError:
            print('You nead to input a number from 1 to 12. Try again...')
        else:
            if month != 2:
                if day < 31:
                    return True
                elif days_in_month(month) == '31 days' and day < 32:
                    return True
                else:
                    print('It is not correct day.')
            else:
                if day < 29:
                    return True
                elif years(year) and day < 30:
                    return True
                else:
                    print('It is not correct day.')


print(correct_data())
