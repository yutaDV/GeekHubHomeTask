'''TASK #4 Write a script that combines three dictionaries
by updating the FIRST one (you can use dicts from the
previous task)'''

dict_1 = {'foo': 'bar', 'bar': 'buz'}
dict_2 = {'dou': 'jones', 'USD': 36}
dict_3 = {'AUD': 19.2, 'name': 'Tom'}

for element in (dict_2, dict_3):
    dict_1.update(element)

print('A new dictionary:', dict_1)
