'''TASK #2 Написати функцію <bank> , яка працює за наступною логікою:
користувач робить вклад у розмірі <a> одиниць строком на <years> років
під <percents> відсотків (кожен рік сума вкладу збільшується на цей
відсоток, ці гроші додаються до суми вкладу і в наступному році на
них також нараховуються відсотки). Параметр <percents> є необов'язковим
і має значення по замовчуванню <10> (10%). Функція повинна принтануть суму,
яка буде на рахунку, а також її повернути (але округлену до копійок).'''


def bank(amount, year, percents=0.1):
    '''The function calculates deposit income'''

    for i in range(year):
        amount += amount * percents
    return round(amount, 2)


while True:
    try:
        amount = float(input("Input the deposit amount:  "))
        year = int(input("For how many years you want to place your deposit:"))
    except ValueError:
        print('This is invalid value. Try again...')
    else:
        break
print(bank(amount, year))
