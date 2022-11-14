'''НT10.   Банкомат 3.0
- Банкомат 3.0
- реалізуйте видачу купюр за логікою видавання найменшої кількості купюр,
  але в межах наявних в банкоматі. Наприклад: 2560 --> 2х1000, 1х500, 3х20.
  Будьте обережні з "жадібним алгоритмом"! Видані купюри також мають бути
  “вилучені” з банкомату. Тобто якщо до операції в банкоматі було 5х1000,
  5х500, 5х20 - має стати 3х1000, 4х500, 2х20.
- як і раніше, поповнення балансу користувача не впливає на кількість купюр.
   Їх кількість може змінювати лише інкасатор.
- обов’язкова реалізація таких дій (назви можете використовувати свої):
При запускі
Вхід
Реєстрація (з перевіркою валідності/складності введених даних)
Вихід
Для користувача
Баланс
Поповнення
Зняття
Історія транзакцій
Вихід на стартове меню
Для інкасатора
Наявні купюри/баланс тощо
Зміна кількості купюр
Повна історія операцій по банкомату (дії всіх користувачів та інкасаторів)
Вихід на стартове меню
- обов’язкове дотримання РЕР8 (якщо самостійно ніяк,
   то https://flake8.pycqa.org/en/latest/ вам в допомогу)
- (опціонально) не лініться і придумайте якусь свою особливу фішку/додатковий
   функціонал, але при умові що основне завдання виконане'''

import sqlite3
import datetime
import time


def welcome_menu():
    ''' the function starts//'''
    menu = {
        'start': 'For login',
        'reg': 'For registration',
        'exit': 'Exit'
    }
    print('\n**********************************************WELCOME TO ATM*******************************************************')
    time.sleep(1)
    print('\nChoice of action')
    for key, value in menu.items():
        print(f'{key} for {value}')
    while True:
        time.sleep(1)
        next_step = input('\nEnter one of the actions listed above:')
        if next_step in menu:
            return next_step
        print('Oops!!! the action is incorrect. Try again...')


def verification(username, user_password):
    '''the function checks the password// верифікація користувача'''

    conn = sqlite3.connect('ATM.db')
    cur = conn.cursor()
    try:
        cur.execute("SELECT * FROM USERS WHERE NAME =:NAME", {'NAME': username})
        if cur.fetchone()[2] == user_password:
            conn.commit
            conn.close()
            return True
        else:
            return False
    except:
        return False


def greeting():
    '''the function requests user data returns verified username
    // вітання користувача'''

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
    '''The function checks the correct name and password for new user'''

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
        'pth': 'Print transaction history for admin',
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
    cur.execute("SELECT * FROM USERS WHERE NAME =:NAME", {'NAME':username})
    user_id = cur.fetchone()[0]
    conn.close()
    return user_id


def menu():
    ''' choice of action, the fuction returns user_action// меню'''

    menu = {
        'balance': 'Look at the balance',
        'top_up': 'Top up the balance',
        'get': 'Receiving money',
        'pth': 'Print transaction history',
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


def banknotes_in_atm():
    '''the function return a list with real par in ATM'''

    result = []
    conn = sqlite3.connect('ATM.db')
    cur = conn.cursor()
    for row in cur.execute("SELECT *FROM ATM_BALANCE"):
        if row[2] > 0:
            result.append(row[0])
    conn.commit()
    conn.close()
    return list(reversed(result))


def min_bank_atm():
    '''the function returns the minimum par in ATM//
    мінімальна купюра в банкоматі'''

    result = []
    conn = sqlite3.connect('ATM.db')
    cur = conn.cursor()
    for row in cur.execute("SELECT *FROM ATM_BALANCE"):
        if row[1] > 0:
            result.append(row[0])
    conn.commit()
    conn.close()
    min_sum = min(result)
    return min_sum


def verification_user_sum():
    '''the function checks whether the entered number is a float and return
    the number// перевірка введеної суми'''

    while True:
        try:
            try_sum = float(input('Enter the amount: '))
        except:
            print("Oops!!! The amount is incorrect. You amount must be a number. Try again...")
        else:
            if try_sum >= min_bank_atm():
                if try_sum // 10 == 0:
                    user_sum = try_sum
                    return (user_sum, 2)
                else:
                    user_sum = try_sum - try_sum % 10
                    print(f'Amount to be processed {user_sum}the rest {try_sum % 10} was returned')
                    return round(user_sum, 2)
            else:
                print(f"Oops!!! The amount is incorrect. You amount must be greater than {min_bank_atm()}. Try again...")


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
    tramsactions('admin', 'Looks at the balance ATM', total_atm(), total_atm())
    return f' total sum = {total_atm()}'


def top_up(id):
    '''The function tops up  the user balance// поповнення балансу'''

    conn = sqlite3.connect('ATM.db')
    cur = conn.cursor()
    user_sum = verification_user_sum()
    cur.execute("SELECT * FROM USERS WHERE ID =:ID", {'ID' :id})
    new_balance = cur.fetchone()[3] + user_sum
    cur.execute("UPDATE USERS SET BALANCE =:BAL WHERE ID =:ID", {'BAL':new_balance, 'ID':id})
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
        new_sum = row[0] * new_number
        all_sum += amount * row[0]
        cursor = conn.cursor()
        cursor.execute("UPDATE ATM_BALANCE SET NUMBER_OF_BILLS =:BIL WHERE DENOMINATION =:DEN",{'BIL':new_number,'DEN':row[0]})
        cursor.execute("UPDATE ATM_BALANCE SET SUM =:SUM WHERE DENOMINATION =:DEN",{'SUM':new_sum,'DEN':row[0]})
    conn.commit()
    conn.close()
    tramsactions('admin', 'Top up the balance', all_sum, total_atm())
    return 'The action is completed'


def take_admin():
    '''The function withdraw from the ATM balance//
    зняття грошей з балансу ATM'''

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
                if row[1] >= amount >= 0:
                    break
                else:
                    print("Not correct value. Try again")
        new_number = row[1] - amount
        new_sum = row[0] * new_number
        all_sum += amount * row[0]
        cursor = conn.cursor()
        cursor.execute("UPDATE ATM_BALANCE SET NUMBER_OF_BILLS =:NUM WHERE DENOMINATION =:DEN", {'NUM':new_sum,'DEN':row[0]})
        cursor.execute("UPDATE ATM_BALANCE SET SUM =:SUM WHERE DENOMINATION =:DEN", {'SUM':new_sum,'DEN':row[0]})
        conn.commit()
    conn.commit()
    conn.close()
    tramsactions('admin', 'Take money of  the ATM balance', all_sum, total_atm())
    return 'The action is completed'


def quantity_limit(par):
    '''the function checks whether such amount of banknotes
    is available in the ATB//допустима кількість купюр в банкоматі'''

    conn = sqlite3.connect('ATM.db')
    cur = conn.cursor()
    for row in cur.execute("SELECT *FROM ATM_BALANCE"):
        if row[0] == par:
            result = row[1]
    conn.commit()
    conn.close()
    return result


def perfect_set(user_sum):
    '''ідеальний набір банкнот для видачі  від бульшого до меншого
     з урахуванням кільклсті банкнот'''

    bancnots = banknotes_in_atm()
    result = []
    for par in bancnots:
        amount = user_sum // par
        amount_atm = quantity_limit(par)
        if amount_atm >= amount > 0:
            result.append((par, amount))
            user_sum = user_sum % par
        if amount > 0 and amount > amount_atm:
            result.append((par, amount_atm))
            user_sum -= (par * amount_atm)
        if user_sum == 0:
            return result, user_sum
    return result, user_sum


def second_set(user_sum):
    '''якщо перший варіант провалився то резервуємо одну наманшу купюру і
     перевіряємо чи все ок, якщо ні то ше мінус 1 (відмінусовані купюри
    додати вкінці, якщо такого не трапилось то Nane)'''

    count = 0
    amount_min = quantity_limit(min_bank_atm())
    for i in range(amount_min):
        if amount_min > 1 and count >= amount_min:
            user_sum -= min_bank_atm()
            count += 1
            result, rest = perfect_set(user_sum)
            if rest == 0:
                if result[-1][0] == min_bank_atm():
                    count += result[-1][1]
                result.pop()
                result.append((min_bank_atm(), count))

                return result
    return None


def third_set(user_sum):
    '''підбір кількості банкнот для зняття, шляхом відмови від найбільшої'''

    bancnots = banknotes_in_atm()
    for i in range(0, len(bancnots)):
        bank_shot = bancnots[i:(len(bancnots))]
        result = []
        test_sum = user_sum
        for p in range(0, len(bank_shot)):
            amount = test_sum // bank_shot[p]
            amount_atm = quantity_limit(bank_shot[p])
            if test_sum == 0:
                return result
            if amount_atm >= amount > 0:
                result.append((bank_shot[p], amount))
                test_sum = test_sum % bank_shot[p]
            if amount > amount_atm:
                result.append((bank_shot[p], amount_atm))
                test_sum -= (bank_shot[p] * amount_atm)


def red_bal_atm(list_pars):
    '''Коригування залишків АТМ після зняття коштів'''

    for element in list_pars:
        conn = sqlite3.connect('ATM.db')
        cur = conn.cursor()
        for row in cur.execute("SELECT *FROM ATM_BALANCE"):
            if row[0] == element[0]:
                new_number = row[1] - element[1]
                new_sum = row[0] * new_number
                cursor = conn.cursor()
                cursor.execute("UPDATE ATM_BALANCE SET NUMBER_OF_BILLS =:NUM WHERE DENOMINATION =:PAR",{'NUM':new_number,'PAR':row[0]})
                cursor.execute("UPDATE ATM_BALANCE SET SUM =:SUM WHERE DENOMINATION =:PAR", {'SUM':new_sum,'PAR':row[0]})
                conn.commit()
        conn.commit()
        conn.close()
    pass


def print_banknots(list_pars):
    '''друк банкнот які було видано'''

    print('You receive:')
    for par in list_pars:
        print(f'{par[1]} banknotes of {par[0]} hryvnias')
    pass


def receiving(id):
    '''The function receis money  the user balance//зняття коштів'''

    conn = sqlite3.connect('ATM.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM USERS WHERE ID =:ID", {'ID': id})
    balance = cur.fetchone()[3]
    if balance < 10:
        return 'Sorry, you cannot do it, this sum is less than 10'
    else:
        while True:
            user_sum = verification_user_sum()
            if user_sum > balance:
                print("Oops! You do not have that amount of money. Try again.")
            if user_sum > total_atm():
                print(f"You can withdraw a maximum {total_atm()} Try again...")
            if user_sum < total_atm() and user_sum < balance:
                super_set, rest = perfect_set(user_sum)
                if rest == 0:
                    break
                elif second_set(user_sum):
                    super_set = second_set(user_sum)
                    break
                elif third_set(user_sum):
                    super_set = third_set(user_sum)
                    break
                else:
                    print(f"Sorry today you can get {user_sum - rest} Try again...")
        new_balance = balance - user_sum
        cur.execute("UPDATE USERS SET BALANCE =:BALANCE WHERE ID =:ID", {'BALANCE':new_balance,'ID':id})
        conn.commit()
        conn.close()
        print(f'')
        red_bal_atm(super_set)
        print_banknots(super_set)
        tramsactions(id, 'Top up the balance', user_sum, new_balance)
        return 'The action is completed'


def trans_history_admin():
    ''' Print transaction history for admin'''

    conn = sqlite3.connect('ATM.db')
    cur = conn.cursor()
    for row in cur.execute("SELECT *FROM TRANSACTIONS"):
        print(row)
    conn.commit()
    conn.close()
    tramsactions('admin', 'Print transaction history', total_atm(), total_atm())
    return 'The action is completed'


def trans_history_user(id):
    ''' Print transaction history for user'''

    conn = sqlite3.connect('ATM.db')
    cur = conn.cursor()
    for row in cur.execute("SELECT *FROM TRANSACTIONS"):
        if id == row[0]:
            print(f'Date - {row[1]}, action - {row[2]},sum {row[3]}, final_sum {row[4]}')
    conn.commit()
    conn.close()
    tramsactions(id, 'Print transaction history', None, None)
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
            print(take_admin())
        if admin_action == 'pth':
            print(trans_history_admin())
        if admin_action == 'exit':
            return
        time.sleep(1)
    print('\n Choose the next action or choose ''exit'' to stop')


def start_user(username):
    '''workflow of user'''

    user_id = return_id(username)
    while True:
        if user_id:
            user_action = menu()
            if user_action == 'balance':
                print(balance(user_id))
            if user_action == 'top_up':
                print(top_up(user_id))
            if user_action == 'pth':
                print(trans_history_user(user_id))
            if user_action == 'get':
                print(receiving(user_id))
            if user_action == 'exit':
                return "Goodbye"
            time.sleep(1)
            print('\n Choose the next action or choose ''exit'' to stop')


def start():
    '''workflow of ATM'''

    while True:
        next_step = welcome_menu()
        if next_step == 'exit':
            return "Good bye"
        if next_step == 'reg':
            username, password = new_user()
            add_new_user(username, password)
        if next_step == 'start':
            username = greeting()
            if username == 'admin':
                start_admin()
            else:
                start_user(username)


if __name__ == "__main__":

    print(start())
   