
'''TASK #6 Write a script to get the maximum
 and minimum VALUE in a dictionary.'''

test_dict = {
    'foo': 345, 'bar': 1415, 'dou': 'jones',
    'USD': 36, 'AUD': -21.5, 'name': 0.8, 'lastname': 'Tom',
    'dddD': 36, 'dAUD': 19.2, 'fname': 0.008, 'hhhhh': True
}

digital_dict = {}
for key, value in test_dict.items():
    if isinstance(value, int) or isinstance(value, float):
        digital_dict[key] = value

print('The maximum VALUE in a dictionary:', max(digital_dict.values()))
print('The minimum VALUE in a dictionary:', min(digital_dict.values()))
