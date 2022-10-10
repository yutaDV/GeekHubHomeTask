'''TASK 1 Write a script which accepts 
a sequence of comma-separated numbers from user 
and generates a list and a tuple with those numbers.'''

numbers = input("Please, type in numbers seperated ONLY by a comma :")
numbers_list = numbers.split(',')
number_tuple = tuple(numbers_list)

print('list version -', numbers_list)
print(f'tuple version - {number_tuple}')
