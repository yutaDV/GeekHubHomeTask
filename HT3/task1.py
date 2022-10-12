'''TASK  #1. . Write a script that will run through a list of tuples
and replace the last value for each tuple. The list of tuples
can be hardcoded. The "replacement" value is entered by user.
The number of elements in the tuples must be different.'''

test_list = [
    ('hey'), ('',), ('ma', 'ke', 'my'),
    ([''], {}, 67), ('d', 5, True), ('', [])
]

value = input('inpur the "replacement" value: ')
buffer = []
our_list = []
for element in test_list:
    buffer = list(element)
    buffer.remove(buffer[-1])
    buffer.append(value)
    element = tuple(buffer)
    our_list.append(element)

print('New list:', our_list)
