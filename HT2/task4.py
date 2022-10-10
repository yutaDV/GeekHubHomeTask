'''TASK #4. Write a script which accepts a <number> from user and
then <number> times asks user for string input. At the end script
must print out result of concatenating all <number> strings.'''
number = int(input("Input a number:"))
result = ''
x = ''
for i in range(number):
    x = input('Please, input a string:  ')
    result = result + x
    i += 1

print(f'Your text: {result}')
