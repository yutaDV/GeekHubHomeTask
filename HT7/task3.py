'''НT7.3.    ви знаєте таку функцію як <range>. Напишіть свою реалізацію
цієї функції. Тобто щоб її можна було використати у вигляді:
    for i in my_range(1, 10, 2):
        print(i)
    1
    3
    5
    7
    9
P.S. Повинен вертатись генератор.
P.P.S. Для повного розуміння цієї функції - можна почитати документацію по ній:
 https://docs.python.org/3/library/stdtypes.html#range
P.P.P.S Не забудьте обробляти невалідні
ситуації (типу range(1, -10, 5) тощо).'''


def my_range(start: int, stop: int, step=1):

    if step == 0:
        raise Exception('arg 3 must not be zero')
    result = []
    if step > 0 and start >= stop:
        while start < stop:
            result.append(start)
            start += step
        return result
    if step < 0 and start > stop:
        while start >= stop:
            result.append(start)
            start += step
        return result
    else:
        raise Exception('incorrect arguments are entered')


for i in my_range(10, 0, -1):
    print(i)
