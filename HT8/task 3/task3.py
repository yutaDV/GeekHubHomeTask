'''НT8.3.   Програма-банкомат.
   Використовуючи функції створити програму з наступним функціоналом:
      - підтримка 3-4 користувачів, які валідуються парою ім'я/пароль
      (файл <users.CSV>);
      - кожен з користувачів має свій поточний баланс
      (файл <{username}_balance.TXT>) та історію транзакцій
      (файл <{username_transactions.JSON>);
      - є можливість як вносити гроші, так і знімати їх. Обов'язкова
      перевірка      введених даних (введено цифри; знімається
      не більше, ніж є на рахунку і т.д.).
   Особливості реалізації:
      - файл з балансом - оновлюється кожен раз при зміні балансу
        (містить просто цифру з балансом);
      - файл - транзакціями - кожна транзакція у вигляді JSON рядка
         додається в кінець файла;
      - файл з користувачами: тільки читається. Але якщо захочете
          реалізувати функціонал додавання нового користувача
          - не стримуйте себе :)
   Особливості функціонала:
      - за кожен функціонал відповідає окрема функція;
      - основна функція - <start()> - буде в собі містити весь
         workflow банкомата:
      - на початку роботи - логін користувача (програма запитує ім'я/пароль).
        Якщо вони неправильні - вивести повідомлення про це і закінчити роботу
       (хочете - зробіть 3 спроби, а потім вже закінчити роботу
             - все на ентузіазмі :))
      - потім - елементарне меню типн:
        Введіть дію:
           1. Подивитись баланс
           2. Поповнити баланс
           3. Вихід
      - далі - фантазія і креатив, можете розширювати функціонал,
       але основне завдання має бути повністю реалізоване :)
    P.S. Увага! Файли мають бути саме вказаних форматів
         (csv, txt, json відповідно)
    P.S.S. Добре продумайте структуру програми та функцій'''

import csv
import json
import datetime


def verification(username, user_password):
    ''' the function checks the password'''

    with open('users.csv', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['user_name'] == username and row['password'] == user_password:
                return True
        return False


def greeting():
    '''the function requests user data returns verified username'''

    attempt = 0
    while attempt < 3:
        username = input('Please, enter your user name:  ')
        user_password = input('Please, enter your password:  ')
        if verification(username, user_password):
            return username
        else:
            print("Oops!!! Username or password is incorrect. Try again... ")
            attempt += 1
    print('The entered data is incorrect, contact the bank')
    return None


def menu():
    ''' choice of action, the fuction returns user_action'''
    menu = {
        'balance': 'Look at the balance',
        'top_up': 'Top up the balance',
        'get': 'Receiving money',
        'exit': 'Exit'
    }
    while True:
        print('Please, choice of action')
        for key, value in menu.items():
            print(f'{key} for {value}')
        user_action = input('Enter one of the actions listed above:')
        if user_action in menu:
            return user_action
        else:
            print('Oops!!! the action is incorrect. Try again...')


def balance(username):
    '''The function looks at the balance'''

    with open(f'{username}_balance.txt') as file:
        result = file.read()
    to_json = {
        'time': f'{datetime.datetime.now()}',
        'action': 'Look at the balance',
        'balance': result
    }
    with open(f'json.{username}_transactions.JSON', 'a') as file:
        json.dump(to_json, file)
        return f'Your belance:{result}'


def top_up(username):
    '''The function tops up  the user balance'''

    while True:
        try:
            user_sum = float(input('Enter the top-up amount: '))
            break
        except:
            print("Oops!!! The amount is incorrect. Try again... ")
    file_name = f'{username}_balance.txt'
    with open(file_name) as file:
        user_balance = float(file.read())
    result = user_balance + user_sum
    with open(file_name, 'w') as file:
        file.write(f'{result}')
    to_json = {
        'time': f'{datetime.datetime.now()}',
        'action': 'Top up the balance',
        'top_up_sum': user_sum, 'finaly_balance': result
    }
    with open(f'json.{username}_transactions.JSON', 'a') as file:
        json.dump(to_json, file)
        return result


def receiving(username):
    '''The function receis money  the user balance'''

    with open(f'{username}_balance.txt') as file:
        user_balance = float(file.read())
    while True:
        try:
            user_sum = float(input('What amount of money you want to receive: '))
        except:
            print("Oops!!! The amount is incorrect. Try again... ")
        else:
            if user_sum <= user_balance:
                break
            else:
                print("Oops!!! You do not have that amount of money. Try again... ")
    result = user_balance - user_sum
    with open(f'{username}_balance.txt', 'w') as file:
        file.write(f'{result}')
    to_json = {
        'time': f'{datetime.datetime.now()}',
        'action': 'Receiving money',
        'top_up_sum': user_sum, 'finaly_balance': result
    }
    with open(f'json.{username}_transactions.JSON', 'a') as file:
        json.dump(to_json, file)
        return result


def start():
    '''workflow of ATM'''

    username = greeting()
    if username:
        user_action = menu()
    else:
        return "The end"
    if user_action == 'exit':
        return "Good bye"
    else:
        return "Good bye"


if __name__ == "__main__":
    print(balance('fox'))
