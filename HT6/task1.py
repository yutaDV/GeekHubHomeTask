'''НT1. Створіть функцію, всередині якої будуть записано СПИСОК
із п'яти користувачів (ім'я та пароль). Функція повинна приймати
три аргументи: два - обов'язкових (<username> та <password>)
і третій - необов'язковий параметр <silent> (значення за замовчуванням
- <False>).Логіка наступна:
    якщо введено правильну пару ім'я/пароль - вертається True;
    якщо введено неправильну пару ім'я/пароль:
        якщо silent == True - функція повертає False
        якщо silent == False - породжується виключення LoginException
        (його також треба створити =))"'''


def verification(username, password, silent=False):
    '''The function checks the correctness of the entered password'''

    zoo_data = [
        {'cat': 'mouse'}, {'hare': 'carrot'},
        {'fox': 'hare'}, {'wolf': 'fox'}, {'bear': 'honey'}
    ]
    for element in zoo_data:
        if element.get(username) == password:
            return True
        else:
            if silent is True:
                return False
            elif silent is False:
                raise Exception("Sorry, not correct your login or password")


username = input('Please, enter your username:  ')
password = input('Please, enter your password:  ')
try:
    print(verification(username, password))
except Exception as e:
    print(f'Goodbye {e}')
