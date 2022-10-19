'''TASK #6 Написати функцію, яка буде реалізувати логіку циклічного зсуву
елементів в списку. Тобто функція приймає два аргументи: список і величину
зсуву (якщо ця величина додатна - пересуваємо з кінця на початок,
якщо від'ємна - навпаки - пересуваємо елементи з початку списку в його кінець).
   Наприклад:
   fnc([1, 2, 3, 4, 5], shift=1) --> [5, 1, 2, 3, 4]
   fnc([1, 2, 3, 4, 5], shift=-2) --> [3, 4, 5, 1, 2] '''


def shift():

    while True:
        values = input("Please, type values seperated ONLY by a comma :")
        our_list = values.split(',')
        try:
            shift = int(input("Input a number for shift:  "))
        except ValueError:
            print('This is invalid value. Input a number:')
        else:
            if shift <= len(our_list):
                break
            else:
                print('This is invalid value. Try again:')
    new_list = our_list[-shift:] + our_list[:-shift]
    return new_list


print(shift())
