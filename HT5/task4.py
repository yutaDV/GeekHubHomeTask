'''TASK #4 Написати функцію <prime_list>, яка прийматиме 2 аргументи - початок
і кінець діапазона, і вертатиме список простих чисел всередині цього діапазона.
Не забудьте про перевірку на валідність введених даних та у випадку
невідповідності - виведіть повідомлення.'''


def prime_list():

    while True:
        try:
            number_1 = int(input("Input the first number:  "))
            number_2 = int(input("Input the second number:  "))
        except ValueError:
            print('This is invalid value. Input a number:')
        else:
            if number_1 >= 0 and number_2 >= 0 and number_1 <= number_2:
                break
            else:
                print('This is invalid value. Try again:')
    result = []
    for number in range(number_1, number_2 + 1):
        divisor = 0
        for i in range(2, number // 2 + 1):
            if number % i == 0:
                divisor += 1
        if divisor == 0 and number > 1:
            result.append(number)
    return result


print(prime_list())
