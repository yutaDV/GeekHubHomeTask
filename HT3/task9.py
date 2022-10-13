'''TASK #9 Користувачем вводиться початковий і кінцевий рік. Створити цикл,
    який виведе всі високосні роки в цьому проміжку (границі включно).
    P.S. Рік є високосним, якщо він кратний 4, але не кратний 100,
    а також якщо він кратний 400.'''

while True:
    try:
        first_year = int(input("Please, input the first year:  "))
        second_year = int(input("Please, input the second year:  "))
        break
    except ValueError:
        print('Oops!!! That was no valid number. Try again...')

print(f"Between {first_year}  and {second_year} we have next leap years:  ")

for year in range(first_year, second_year + 1):
    if year % 400 == 0:
        print(year)
    else:
        if year % 4 == 0 and year % 100 != 0:
            print(year)
