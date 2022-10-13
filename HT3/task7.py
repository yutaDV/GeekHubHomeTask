
'''TASK #7 Write a script which accepts a <number>(int) from
user and generates dictionary in range <number>
where key is <number> and value is <number>*<number>
e.g. 3 --> {0: 0, 1: 1, 2: 4, 3: 9}'''

while True:
    try:
        number = int(input("Please, enter a number:  "))
        break
    except ValueError:
        print("Oops!!! That was no valid number. Try again... ")

our_dict = {}
for i in range(number + 1):
    our_dict[i] = i * i
    i += i

print('Our dictionary:', our_dict)
