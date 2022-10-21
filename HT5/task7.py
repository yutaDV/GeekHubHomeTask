'''TASK #7 Написати функцію, яка приймає на вхід список (через кому),
підраховує кількість однакових елементів у ньому і виводить результат.
Елементами списку можуть бути дані будь-яких типів.
    Наприклад:
    1, 1, 'foo', [1, 2], True, 'foo', 1, [1, 2] ---->
    "1 -> 3, foo -> 2, [1, 2] -> 2, True -> 1"'''


def copies(test_list):

    newlist = []
    for element in test_list:
        newlist.append((element, (type(element))))
    original_list = []
    for element in newlist:
        if element not in original_list:
            original_list.append(element)
    result = ''
    for element in original_list:
        result += f'{element[0]} -> {newlist.count(element)}, '
    return f'{result}'


test_list = [
    'True', False, 1, 1, 'foo', [1, 2], 56, 55, -111,
    True, {5: 2}, 'foo', [1, 2], True, {5: 2}, -111, 0
]
print(copies(test_list))
