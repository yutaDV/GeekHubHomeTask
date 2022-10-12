'''TASK #9 Користувачем вводиться початковий і кінцевий рік. Створити цикл,
    який виведе всі високосні роки в цьому проміжку (границі включно).
    P.S. Рік є високосним, якщо він кратний 4, але не кратний 100,
    а також якщо він кратний 400.'''

number = int(input("Please, input a number:  "))

if number < 17:
    print('Sorry, I do not have any result for you')
else:
    print('your results:')
    for i in range(number):
        if i > 0 and i % 17 == 0:
            print(i)
