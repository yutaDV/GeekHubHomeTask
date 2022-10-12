'''TASK #5 Write a script to remove values duplicates
from dictionary. Feel free to hardcode your dictionary.'''

test_dict = {
    'foo': 'bar', 'bar': True, 'dou': 'jones',
    'USD': 36, 'AUD': 19.2, 'name': 'Tom', 'lastname': 'Tom',
    'dddD': 36, 'dAUD': 19.2, 'fname': 'GTom', 'hhhhh': True
}

original_dict = {}
for key, value in test_dict.items():
    if value not in original_dict.values():
        original_dict[key] = value

print('A original dictionary:', original_dict)
