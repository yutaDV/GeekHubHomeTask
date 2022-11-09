'''НT9.   Банкомат 2.0
- усі дані зберігаються тільки в sqlite3 базі даних у відповідних таблицях.
      Більше ніяких файлів. Якщо в попередньому завданні ви добре продумали
      структуру програми то у вас не виникне проблем швидко адаптувати
       її до нових вимог.
- на старті додати можливість залогінитися або створити нового
      користувача (при створенні нового користувача, перевіряється
      відповідність логіну і паролю мінімальним вимогам. Для перевірки
      створіть окремі функції)
- в таблиці з користувачами також має бути створений унікальний користувач
     -інкасатор, який матиме розширені можливості (домовимось, що логін/пароль
      будуть admin/admin щоб нам було простіше перевіряти)
- банкомат має власний баланс
- кількість купюр в банкоматі обмежена (тобто має зберігатися номінал
       та кількість). Номінали купюр - 10, 20, 50, 100, 200, 500, 1000
- змінювати вручну кількість купюр або подивитися їх залишок в банкоматі
        може лише інкасатор
- користувач через банкомат може покласти на рахунок лише суму кратну
        мінімальному номіналу що підтримує банкомат. В іншому випадку
        - повернути "здачу" (наприклад при поклажі 1005 --> повернути 5).
        Але це не має впливати на баланс/кількість купюр банкомату, лише
        збільшується баланс користувача (моделюємо наявність двох незалежних
         касет в банкоматі - одна на прийом, інша на видачу)
- зняти можна лише в межах власного балансу,
        але не більше ніж є всього в банкоматі.
- при неможливості виконання якоїсь операції - вивести повідомлення з причиною
       (невірний логін/пароль, недостатньо коштів на рахунку, неможливо видати
       суму наявними купюрами тощо.)
- файл бази даних з усіма створеними таблицями і даними також додайте
        в репозиторій, що б ми могли його використати'''

import sqlite3
import datetime
import time


def user_active():
    ''' the function asks if the user is new// запит щодо існування користувача'''

    print('**********************************************WELCOME TO ATM*******************************************************')
    while True:
        user = input('Are you an active ATM user? Are you an active ATM user? Enter YES (for existing user) NO (for new): ')
        if user.lower() == 'yes':
            return True
        if user.lower() == 'no':
            return False
        print("Oops!!! The answer is incorrect. Enter YES (for existing user) NO (for new). Try again...")


def verification(username, user_password):
    '''the function checks the password// верифікація користувача'''

    conn = sqlite3.connect('ATM.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM USERS WHERE NAME =:NAME", {'NAME': username})
    if cur.fetchone()[2] == user_password:
        conn.commit
        conn.close()
        return True
    else:
        return False

def greeting():
    '''the function requests user data returns verified username // вітання користувача'''

    attempt = 0
    while attempt < 3:
        username = input('Please, enter your user name:  ')
        user_password = input('Enter your password:  ')
        if verification(username, user_password):
            return username
        else:
            print("\nOops!!! Username or password is incorrect. Try again... ")
            attempt += 1
    print('The entered data is incorrect, contact the bank')
    return 'Goodbye!!!'


def validation_password(username, password):
    '''The function checks the correct name and password'''

    password_digit = 0
    for letter in password:
        if letter.isdigit():
            password_digit += 1
    while True:
        if len(username) < 3:
            print("Your name is too short ")
            return False
        elif len(username) > 50:
            print("Your name is too long ")
            return False
        elif len(password) < 8:
            print("Your password is too short ")
            return False
        if password_digit == 0:
            print("password must have at least one digit ")
            return False
        elif username in password:
            print("The password cannot contain a name ")
            return False
        return True


def new_user():
    ''' The function registrations of new user// рестрація нового
     користувача первірка паролю та імені на валідність'''
    while True:
        username = input('Please, enter your username:  ')
        password = input('Please, enter your password:  ')
        if validation_password(username, password):
            return username, password
        print("Oops!!! The answer is incorrect. Try again...")
    return username, password


def tramsactions(id_user, action, sum_action, final_sum):
    '''The commits transactions'''

    conn = sqlite3.connect('ATM.db')
    cursor = conn.cursor()
    tpans_params = (id_user, f'{datetime.datetime.now()}', action, sum_action, final_sum,)
    cursor.execute("INSERT INTO TRANSACTIONS VALUES (?,?,?,?,?)", tpans_params)
    conn.commit()
    conn.close()
    return


def add_new_user(username, user_password):
    ''' The function adds a new user// функція
    додає дані нового користувача до БД'''
    conn = sqlite3.connect('ATM.db')
    cursor = conn.cursor()
    sum_id = 0
    for row in cursor.execute("SELECT *FROM USERS"):
        sum_id += 1
    params = (sum_id + 1, username, user_password, 0, 'False')
    cursor.execute("INSERT INTO USERS VALUES (?,?,?,?,?)", params)
    conn.commit()
    conn.close()
    print('Your registration was successful!!')
    return True


def admin_menu():
    ''' choice of action, the fuction returns user_action// меню інкасатора'''
    admin_menu = {
        'balance': 'Look at the balance_ATM',
        'top_up': 'Top up the balance_ATM',
        'get': 'Receiving money_ATM',
        'exit': 'Exit'
    }
    time.sleep(1)
    print('\nChoice of action')
    for key, value in admin_menu.items():
        print(f'{key} for {value}')
    while True:
        time.sleep(1)
        admin_action = input('\nEnter one of the actions listed above:')
        if admin_action in admin_menu:
            return admin_action
        print('Oops!!! the action is incorrect. Try again...')


def return_id(username):
    '''The function returns  the user_ID'''

    conn = sqlite3.connect('ATM.db')
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM USERS WHERE NAME = '{username}'")
    user_id = cur.fetchone()[0]
    conn.close()
    return user_id


def menu():
    ''' choice of action, the fuction returns user_action// меню'''
    menu = {
        'balance': 'Look at the balance',
        'top_up': 'Top up the balance',
        'get': 'Receiving money',
        'exit': 'Exit'
    }
    time.sleep(1)
    print('\nChoice of action')
    for key, value in menu.items():
        print(f'{key} for {value}')
    while True:
        time.sleep(1)
        user_action = input('\nEnter one of the actions listed above:')
        if user_action in menu:
            return user_action
        print('Oops!!! the action is incorrect. Try again...')


def verification_user_sum():
    '''the function checks whether the entered number is a float and return
    the number// перевірка введеної суми'''

    while True:
        try:
            try_sum = float(input('Enter the amount: '))
        except:
            print("Oops!!! The amount is incorrect. You amount must be a number. Try again...")
        else:
            if try_sum >= 10:
                if try_sum // 10 == 0:
                    user_sum = try_sum
                    return (user_sum, 2)
                else:
                    user_sum = try_sum - try_sum % 10
                    print(f'Amount to be processed {user_sum}the rest {try_sum % 10} was returned')
                    return round(user_sum, 2)
            else:
                print("Oops!!! The amount is incorrect. You amount must be greater than 10. Try again...")


def balance(id):
    '''The function looks at the balance// функція перевірки балансу'''

    conn = sqlite3.connect('ATM.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM USERS WHERE ID =:ID", {'ID': id})
    result = cur.fetchone()[3]
    conn.commit()
    conn.close()
    tramsactions(id, 'Looks at the balance', result, result)
    return f'Your belance:{result}'


def total_atm():
    '''The function returns the total sum ATM//залишок в банкоматі'''

    conn = sqlite3.connect('ATM.db')
    cur = conn.cursor()
    cur.execute('SELECT SUM FROM ATM_BALANCE')
    result = cur.fetchall()
    total_atm = 0
    for x in result:
        total_atm += x[0]
    conn.close()
    return total_atm


def balance_admin():
    '''The function looks at the balance ATM for admin//
    функція перевірки балансу ATM'''

    conn = sqlite3.connect('ATM.db')
    cur = conn.cursor()
    for row in cur.execute("SELECT *FROM ATM_BALANCE"):
        print(row)
    conn.commit()
    conn.close()
    tramsactions('ATM', 'Looks at the balance ATM', total_atm(), total_atm())
    return f' total sum = {total_atm()}'


def top_up(id):
    '''The function tops up  the user balance// поповнення балансу'''

    conn = sqlite3.connect('ATM.db')
    cur = conn.cursor()
    user_sum = verification_user_sum()
    cur.execute("SELECT * FROM USERS WHERE ID =:ID", {'ID':id})
    new_balance = cur.fetchone()[3] + user_sum
    cur.execute(f"UPDATE USERS SET BALANCE = {new_balance} WHERE ID = {id}")
    conn.commit()
    conn.close()
    tramsactions(id, 'Top up the balance', user_sum, new_balance)
    return 'The action is completed'


def top_up_admin():
    '''The function tops up  the ATM balance// поповнення балансу ATM'''

    conn = sqlite3.connect('ATM.db')
    cur = conn.cursor()
    all_sum = 0
    for row in cur.execute("SELECT *FROM ATM_BALANCE"):
        while True:
            try:
                amount = int(input(f'Input number top up for {row[0]} - '))
            except:
                print("Not correct value. Try again")
            else:
                if amount >= 0:
                    break
                else:
                    print("Not correct value. Try again")
        new_number = row[1] + amount
        new_sum = row[2] / row[1] * new_number
        all_sum += new_sum
        cursor = conn.cursor()
        cursor.execute(f"UPDATE ATM_BALANCE SET NUMBER_OF_BILLS = {new_number} WHERE DENOMINATION = {row[0]}")
        cursor.execute(f"UPDATE ATM_BALANCE SET SUM = {new_sum} WHERE DENOMINATION = {row[0]}")
        conn.commit()
    conn.commit()
    conn.close()
    tramsactions('ATM', 'Top up the balance', all_sum, total_atm())
    return 'The action is completed'


def receiving(id):
    '''The function receis money  the user balance//зняття коштів'''

    conn = sqlite3.connect('ATM.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM USERS WHERE ID =:ID", {'ID':id})
    balance = cur.fetchone()[3]
    if balance < 10:
        return 'Sorry, you cannot do it!!'
    else:
        while True:
            user_sum = verification_user_sum()
            if user_sum < total_atm() and user_sum < balance:
                break
            if user_sum > balance:
                print("Oops! You do not have that amount of money. Try again.")
            if user_sum > total_atm():
                print(f"You can withdraw a maximum {total_atm()} Try again...")
        new_balance = balance - user_sum
        cur.execute(f"UPDATE USERS SET BALANCE = {new_balance} WHERE ID = {id}")
        conn.commit()
        conn.close()
        tramsactions(id, 'Top up the balance', user_sum, new_balance)
        return 'The action is completed'


def start_admin():
    '''workflow of ATM for admin'''

    while True:
        admin_action = admin_menu()
        if admin_action == 'balance':
            print(balance_admin())
        if admin_action == 'top_up':
            print(top_up_admin())
        if admin_action == 'get':
            print("It will be in the next hometask)))")
        if admin_action == 'exit':
            return
        time.sleep(1)
    print('\n Choose the next action or choose ''exit'' to stop')


def start():
    '''workflow of ATM'''

    if user_active() is False:
        username, password = new_user()
        add_new_user(username, password)
    username = greeting()
    user_id = return_id(username)
    if username == 'admin':
        start_admin()
        return "Good bye"
    else:
        while True:
            if user_id:
                user_action = menu()
                if user_action == 'balance':
                    print(balance(user_id))
                if user_action == 'top_up':
                    print(top_up(user_id))
                if user_action == 'get':
                    print(receiving(user_id))
                if user_action == 'exit':
                    return "Goodbye"
                time.sleep(1)
                print('\n Choose the next action or choose ''exit'' to stop')


if __name__ == "__main__":

    print(start())
