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


def my_range(a, b=None, step=1):

    if not isinstance(step, int):
        raise Exception('object cannot be interpreted as an integer')
    if b is None:
        if not isinstance(a, int):
            raise Exception('object cannot be interpreted as an integer')
        stop, start = a, 0
    else:
        if not isinstance(a, int) or not isinstance(b, int):
            raise Exception('object cannot be interpreted as an integer')
        start, stop = a, b
    if step == 0:
        raise Exception('arg 3 must not be zero')
    if step > 0 and stop > start:
        while start < stop:
            yield start
            start += step
    elif step < 0 and start > stop:
        while start > stop:
            yield start
            start += step
    else:
        raise Exception('Incorrect data entered')


for i in my_range(10, 0, -3):
    print(i)
