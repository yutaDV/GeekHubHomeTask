'''TASK #7 Написати функцію, яка приймає на вхід список (через кому),
підраховує кількість однакових елементів у ньому і виводить результат.
Елементами списку можуть бути дані будь-яких типів.
    Наприклад:
    1, 1, 'foo', [1, 2], True, 'foo', 1, [1, 2] ---->
    "1 -> 3, foo -> 2, [1, 2] -> 2, True -> 1"'''


def copies(test_list):

    newlist_0 = [x if x is not True else 'True' for x in test_list]
    newlist = [x if x is not False else 'False' for x in newlist_0]
    oreginal_list = []
    for element in newlist:
        if element not in oreginal_list:
            oreginal_list.append(element)
    result = ''
    for element in oreginal_list:
        if element is True:
            result += f'{True} -> {newlist.count(element)}, '
        if element is False:
            result += f'{False} -> {newlist.count(element)}, '
        else:
            result += f'{element} -> {newlist.count(element)}, '
    return f'{result}'


test_list = [
    False, 1, 1, 'foo', [1, 2], 'foo', 56, 55, -111,
    True, {5: 2}, 'foo', [1, 2], True, {5: 2}, -111, 0
]
print(copies(test_list))
