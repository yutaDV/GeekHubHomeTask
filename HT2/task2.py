'''TASK  #2. Write a script which accepts two sequences of
comma-separated colors from user. Then print out a set containing all
the colors from color_list_1 which are not present in color_list_2.'''

sequences_1 = input("Please, type in colors seperated ONLY by a comma:")
sequences_2 = input("Type in colors seperated ONLY by a comma, the next sequenc:")
colorlist_1 = set(sequences_1.split(','))
colorlist_2 = set(sequences_2.split(','))

result = colorlist_1.difference(colorlist_2)

print(f'colors only in the firste color list are {result}')
