'''TASK  #2 Write a script to remove empty elements from a list.
    Test list: [(), ('hey'), ('',), ('ma', 'ke', 'my'), [''], {},
    ['d', 'a', 'y'], '', []]'''

test_list = [
    (), ('hey'), ('',), ('ma', 'ke', 'my'),
    [''], {}, ['d', 'a', 'y'], '', []
]

list_without_empty = []
for element in test_list:
    if len(element) != 0:
        list_without_empty.append(element)

print('List without empty elements: ', list_without_empty)
