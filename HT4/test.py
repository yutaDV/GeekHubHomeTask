'''TASK # 1. Написати функцiю season, яка приймає один аргумент
(номер мiсяця вiд 1 до 12) та яка буде повертати пору року,
до якої цей мiсяць належить (зима, весна, лiто або осiнь).
У випадку некоректного введеного значення -
виводити відповідне повідомлення.'''


def season():
    '''Function accepts a month number and returns the season of this month.'''

    while True:
        try:
            month = int(input("Please, input a month number:  "))
        except ValueError:
            print('You nead to input a number from 1 to 12. Try again...')
        else:
            if month in range(1, 13):
                break
            else:
                print('This number is not from 1 to 12. Try again...')
    seasons = {
        'spring': [3, 4, 5],
        'summer': [6, 7, 8],
        'aoutumn': [9, 10, 11],
        'winter': [12, 1, 2]
    }
    for key, value in seasons.items():
        if month in value:
            return f'The month  number {month} is in {key}'


print(season())