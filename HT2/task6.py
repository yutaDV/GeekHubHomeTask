'''TASK  #6. Write a script to check whether a value
 from user input is contained in a group of values.
e.g. [1, 2, 'u', 'a', 4, True] --> 2 --> True
     [1, 2, 'u', 'a', 4, True] --> 5 --> False'''

value = input("Please, input a value:")
group_of_values = [1, 2, 'u', 'a', 'Y', 4, True, 5]

string_group = []
for i in range(len(group_of_values)):
    i = str(group_of_values[i])
    string_group.append(i)

if value in string_group:
    print(True)
else:
    print(False)
