'''TASK  #1. . Write a script that will run through a list of tuples
and replace the last value for each tuple. The list of tuples
can be hardcoded. The "replacement" value is entered by user.
The number of elements in the tuples must be different.'''
'''Напишіть сценарій, який запускатиме список кортежів
і замінюватиме останнє значення для кожного кортежу.
Список кортежів може бути жорстко закодований.
Значення "заміщення" вводиться користувачем.
Кількість елементів у кортежах має бути різною'''

seperated = input("Please, input in ONLY numbers seperated ONLY by a comma :")
seperated = seperated.split(',')
numbers_list = []

for i in range(len(seperated)):
	i = int(seperated[i])
	numbers_list.append(i)

number_tuple = tuple(numbers_list)

print('list version -', numbers_list)
print(f'tuple version - {number_tuple}')
