'''TASK  #3. Write a script which accepts a <number>
 from user and print out a sum of the first <number>
positive integers.'''

number = int(input("Please, input a value:"))
result = sum(range(number + 1))
print(f'the sum of the first {number} is {result}')
