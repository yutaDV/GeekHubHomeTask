'''TASK  #7. Write a script to concatenate all
 elements in a list into a string and print it.
 List must include both strings
 and integers and must be hardcoded.'''

our_list = [1, 2, 'u', '5', 'a', 'Y', 4, '&', 5, 7.07]
result = ''
for element in our_list:
    result += str(element)
print(f'your string: {result}')
