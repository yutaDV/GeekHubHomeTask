'''TASK # 4.  Наприклад маємо рядок --> "f98neroi4nr0c3n30irn03ien3c0rfe
 kdno400we(nw,kowe%00koi!jn35pijnp4 6ij7k5j78p3kj546p4 65jnpoj35po6j345"
 -> просто потицяв по клавi =)
Створіть ф-цiю, яка буде отримувати довільні рядки на
зразок цього та яка обробляє наступні випадки:
-  якщо довжина рядка в діапазоні 30-50 (включно)
-> прiнтує довжину рядка, кiлькiсть букв та цифр
-  якщо довжина менше 30 -> прiнтує суму всіх чисел
та окремо рядок без цифр та знаків лише з буквами (без пробілів)
-  якщо довжина більше 50 -> щось вигадайте самі, проявіть фантазію =)
-> повернути зеркальний рядок'''


def string_conversion():
    '''Function converts a string.'''

    our_string = input('Please, enter a string:  ')
    if len(our_string) > 50:
        new_string = ''
        for i in range(len(our_string) - 1, -1, -1):
            new_string += our_string[i]
        print(f' New string:  {new_string}')
    elif len(our_string) < 30:
        if len(our_string) == 0:
            print('There is not any results for you!')
        else:
            new_string = ''
            our_sum = 0
            for letter in our_string:
                if letter.isalpha():
                    new_string += letter
                elif letter.isdigit():
                    our_sum += int(letter)
            print(f' New string: {new_string}')
            print(f' The sum of numbers: {our_sum}')
    else:
        numbers = 0
        letters = 0
        for letter in our_string:
            if letter.isalpha():
                letters += 1
            elif letter.isdigit():
                numbers += 1
        print(f'The len of string: {len(our_string)}')
        print(f'The amount of numbers: {numbers}')
        print(f'The amount of letters: {letters}')


string_conversion()
