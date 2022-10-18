'''TASK #3 Написати функцию <is_prime>, яка прийматиме 1 аргумент - число від
 0 до 1000, и яка вертатиме True, якщо це число просте і False - якщо ні.'''


def is_prime():
    '''The function checks whether a number is prima'''

    while True:
        try:
            number = int(input("Input a number from 0 to 1000:  "))
        except ValueError:
            print('This is invalid value. Input a number from 0 to 1000:')
        else:
            if number > 0:
                break
            else:
                print('This is invalid value. Input a number from 0 to 1000:')
    divisor = 0
    for i in range(2, number - 1):
        if number % i == 0:
            divisor += 1
    if number < 2:
        return 'this number is neither prime nor complex '
    elif divisor == 0:
        return True
    else:
        return False


print(is_prime())
