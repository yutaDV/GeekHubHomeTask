'''TASK  #1. . Write a script which accepts a sequence
of comma-separated numbers from user and generates
a list and a tuple with those numbers.'''

seperated = input("Please, input in ONLY numbers seperated ONLY by a comma :")
seperated = seperated.split(',')
numbers_list = []

for i in range(len(seperated)):
    i = int(seperated[i])
    numbers_list.append(i)

number_tuple = tuple(numbers_list)

print('list version -', numbers_list)
print(f'tuple version - {number_tuple}')
