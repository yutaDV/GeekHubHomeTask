'''TASK 1 Write a script which accepts 
a sequence of comma-separated numbers from user 
and generates a list and a tuple with those numbers.'''


def copies(test_list):

    oreginal_list = []
    for i in range(len(test_list)):
        if test_list[i] not in oreginal_list:
            oreginal_list.append(test_list[i])
    return oreginal_list


test_list = [1, 1, 'foo', [1, 2], False, {5: 2}, 'foo', [1, 2], True, {5: 2}]
print(copies(test_list))
