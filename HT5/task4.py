'''TASK #4 Написати функцію <prime_list>, яка прийматиме 2 аргументи - початок
і кінець діапазона, і вертатиме список простих чисел всередині цього діапазона.
Не забудьте про перевірку на валідність введених даних та у випадку
невідповідності - виведіть повідомлення.'''


def prime_list(number_1: int, number_2: int):

    result = []
    for number in range(number_1, number_2 + 1):
        divisor = 0
        for i in range(2, number // 2 + 1):
            if number % i == 0:
                divisor += 1
        if divisor == 0 and number > 1:
            result.append(number)
    return result


while True:
    try:
        number_1 = int(input("Input the first number:  "))
        number_2 = int(input("Input the second number:  "))
    except ValueError:
        print('This is invalid value. Input a number:')
    else:
        if 0 <= number_1 <= number_2 and number_2 >= 0:
            break
        else:
            print('This is invalid value. Try again:')
print(prime_list(number_1, number_2))
