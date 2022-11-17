'''НT11. 3   Банкомат 4.0: переробіть программу з функціонального підходу
програмування на використання класів. Додайте шанс 10% отримати бонус на
 баланс при створенні нового користувача.'''

import sqlite3
import datetime
import time
import random


class Customers:
    '''The class whose objects are ATM users

    Attributes -  username, user_password that identify the user. 
    The user_id attribute is unique and assigned to the client for
    further operations at the ATM. The class contains methods for
    verifying and erasing the user.'''
    user_id = None
    admin_token = False

    def __init__(self, username, user_password):
        self.username = username
        self.user_password = user_password

    def verification(self):
        '''the function verifies the correctness of the entered user
         login and password'''

        conn = sqlite3.connect('ATM.db')
        cur = conn.cursor()
        try:
            cur.execute("SELECT * FROM USERS WHERE NAME =:NAME", {'NAME': self.username})
            if cur.fetchone()[2] == self.user_password:
                conn.commit
                conn.close()
                return True
            else:
                return False
        except:
            return False

    def validation_password(self):
        '''The function checks the correct name and password for а new user'''

        password_digit = 0
        for letter in self.user_password:
            if letter.isdigit():
                password_digit += 1
        while True:
            if len(self.username) < 3:
                print("Your name is too short ")
                return False
            elif len(self.username) > 50:
                print("Your name is too long ")
                return False
            elif len(self.user_password) < 8:
                print("Your password is too short ")
                return False
            if password_digit == 0:
                print("password must have at least one digit ")
                return False
            elif self.username in self.user_password:
                print("The password cannot contain a name ")
                return False
            return True

    def bonus_draw(self):
        '''the function draws 1,000 hryvnias to the balance for a new user'''

        print("\nYou have the honor of winning 1000 hryvnias for your balance")
        time.sleep(1)
        print("Three")
        time.sleep(1)
        print("Two")
        time.sleep(1)
        print("One")
        result = random.randrange(1, 10)
        if result == 1:
            time.sleep(1)
            print('Congratulations!Your balance has been replenished by 1000 hryvnias.')
            return True
        else:
            time.sleep(1)
            print('Money is evil. You are lucky in love.')
            return False

    def new_user(self):
        ''' The function registrations of а new user'''

        if self.validation_password(self.username, self.user_password):
            print("Super!!! You did it.")
            if self.bonus_draw(self):
                self.user_balance = 1000
            else:
                self.user_balance = 0
            print(self.user_balance)
            return True
        else:
            return False
        print("Oops!!! The answer is incorrect. Try again...")

    def add_new_user(self):
        ''' The function adds a new user// функція
        додає дані нового користувача до БД'''

        conn = sqlite3.connect('ATM.db')
        cursor = conn.cursor()
        sum_id = 0
        for row in cursor.execute("SELECT *FROM USERS"):
            sum_id += 1
        params = (sum_id + 1, self.username, self.user_password, self.user_balance, self.admin_token)
        cursor.execute("INSERT INTO USERS VALUES (?,?,?,?,?)", params)
        conn.commit()
        conn.close()
        print('Your registration was successful!!')
        return

    def return_id(self):
        '''The function returns  the user_ID'''

        conn = sqlite3.connect('ATM.db')
        cur = conn.cursor()
        cur.execute("SELECT * FROM USERS WHERE NAME =:NAME", {'NAME': self.username})
        user_id = cur.fetchone()[0]
        conn.close()
        return user_id


class Atm:
    '''A class whose objects are actions that can be performed in ATM

    Attributes - user_id accesses the user's balance
    The class contains methods for checking the increase and decrease
    of the user's balance, the total balance of the Atm.'''

    def __init__(self, user_id):
        self.user_id = user_id
        self.trans = Transactions()

    def verification_user_sum(self):
        '''the function checks whether the entered number is a float and return
        the number'''

        while True:
            try:
                try_sum = float(input('Enter the amount: '))
            except:
                print("Oops!!! The amount is incorrect. You amount must be a number. Try again...")
            else:
                if try_sum >= self.min_bank_atm():
                    if try_sum // 10 == 0:
                        user_sum = try_sum
                        return round(user_sum, 2)
                    else:
                        user_sum = try_sum - try_sum % 10
                        print(f'Amount to be processed {user_sum}the rest {try_sum % 10} was returned')
                        return round(user_sum, 2)
                else:
                    print(f"Oops!!! The amount is incorrect. You amount must be greater than {self.min_bank_atm()}. Try again...")

    def balance(self):
        '''The function looks at the balance// функція перевірки балансу'''

        conn = sqlite3.connect('ATM.db')
        cur = conn.cursor()
        cur.execute("SELECT * FROM USERS WHERE ID =:ID", {'ID': self.user_id})
        result = cur.fetchone()[3]
        conn.commit()
        conn.close()
        self.trans.transactions(self.user_id, 'Looks at the balance', result, result)
        return result

    def top_up(self):
        '''The function tops up  the user balance'''

        conn = sqlite3.connect('ATM.db')
        cur = conn.cursor()
        user_sum = self.verification_user_sum()
        cur.execute("SELECT * FROM USERS WHERE ID =:ID", {'ID': self.user_id})
        user_balance = cur.fetchone()[3] + user_sum
        cur.execute("UPDATE USERS SET BALANCE =:BAL WHERE ID =:ID", {'BAL':user_balance, 'ID': self.user_id})
        conn.commit()
        conn.close()
        self.trans.transactions(self.user_id, 'Top up the balance', user_sum, user_balance)
        return 'The action is completed'

    def perfect_set(self, user_sum):
        '''the function selects the ideal set of banknotes for issuing
        from the largest to the smallest taking into account the number
        of banknotes in the ATM.'''

        bancnots = self.banknotes_in_atm()
        result = []
        for banknote in bancnots:
            amount = user_sum // banknote
            amount_atm = self.quantity_limit(banknote)
            if amount_atm >= amount > 0:
                result.append((banknote, amount))
                user_sum = user_sum % banknote
            if amount > 0 and amount > amount_atm:
                result.append((banknote, amount_atm))
                user_sum -= (banknote * amount_atm)
            if user_sum == 0:
                return result, user_sum
        return result, user_sum

    def second_set(self, user_sum):
        '''The function uses the second method of selecting bills.
        The function reserves the smallest bill for further issuance.'''

        count = 0
        amount_min = self.quantity_limit(self.min_bank_atm())
        for i in range(amount_min):
            if amount_min > 1 and count >= amount_min:
                user_sum -= self.min_bank_atm()
                count += 1
                result, rest = self.perfect_set(user_sum)
                if rest == 0:
                    if result[-1][0] == self.min_bank_atm():
                        count += result[-1][1]
                    result.pop()
                    result.append((self.min_bank_atm(), count))
                    return result
        return None

    def third_set(self, user_sum):
        '''The function uses the third method of selecting bills.
        The function excludes the largest bill from the set.'''

        bancnots = self.banknotes_in_atm()
        for i in range(0, len(bancnots)):
            bank_shot = bancnots[i:(len(bancnots))]
            result = []
            test_sum = user_sum
            for p in range(0, len(bank_shot)):
                amount = test_sum // bank_shot[p]
                amount_atm = self.quantity_limit(bank_shot[p])
                if test_sum == 0:
                    return result
                if amount_atm >= amount > 0:
                    result.append((bank_shot[p], amount))
                    test_sum = test_sum % bank_shot[p]
                if amount > amount_atm:
                    result.append((bank_shot[p], amount_atm))
                    test_sum -= (bank_shot[p] * amount_atm)

    def receiving(self):
        '''The function receis money  the user balance'''

        conn = sqlite3.connect('ATM.db')
        cur = conn.cursor()
        cur.execute("SELECT * FROM USERS WHERE ID =:ID", {'ID': self.user_id})
        balance = cur.fetchone()[3]
        if balance < 10:
            return 'Sorry, you cannot do it, this sum is less than 10'
        else:
            while True:
                user_sum = self.verification_user_sum()
                if user_sum > balance:
                    print("Oops! You do not have that amount of money. Try again.")
                if user_sum > self.total_atm():
                    print(f"You can withdraw a maximum {self.total_atm()} Try again...")
                if user_sum < self.total_atm() and user_sum < balance:
                    super_set, rest = self.perfect_set(user_sum)
                    if rest == 0:
                        break
                    elif self.second_set(user_sum):
                        super_set = self.second_set(user_sum)
                        break
                    elif self.third_set(user_sum):
                        super_set = self.third_set(user_sum)
                        break
                    else:
                        print(f"Sorry today you can get {user_sum - rest} Try again...")
            new_balance = balance - user_sum
            cur.execute("UPDATE USERS SET BALANCE =:BALANCE WHERE ID =:ID", {'BALANCE': new_balance, 'ID': self.user_id})
            conn.commit()
            conn.close()
            self.red_bal_atm(super_set)
            self.print_banknots(super_set)
            self.trans.transactions(self.user_id, 'Top up the balance', user_sum, new_balance)
            return 'The action is completed'

    def trans_history_user(self):
        ''' Print transaction history for user'''

        conn = sqlite3.connect('ATM.db')
        cur = conn.cursor()
        for row in cur.execute("SELECT *FROM TRANSACTIONS"):
            if self.user_id == row[0]:
                print(f'Date - {row[1]}, action - {row[2]},sum {row[3]}, final_sum {row[4]}')
        conn.commit()
        conn.close()
        self.trans.transactions(self.user_id, 'Print transaction history', None, None)
        return 'The action is completed'

    def banknotes_in_atm(self):
        '''the function return a list with real banknotes in ATM'''

        result = []
        conn = sqlite3.connect('ATM.db')
        cur = conn.cursor()
        for row in cur.execute("SELECT *FROM ATM_BALANCE"):
            if row[2] > 0:
                result.append(row[0])
        conn.commit()
        conn.close()
        return list(reversed(result))

    def min_bank_atm(self):
        '''the function returns the minimum banknote in ATM'''

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

    def total_atm(self):
        '''The function returns the total sum ATM'''

        conn = sqlite3.connect('ATM.db')
        cur = conn.cursor()
        cur.execute('SELECT SUM FROM ATM_BALANCE')
        result = cur.fetchall()
        total_atm = 0
        for x in result:
            total_atm += x[0]
        conn.close()
        return total_atm

    def take_admin(self):
        '''The function withdraw from the ATM balance'''

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
            cursor.execute("UPDATE ATM_BALANCE SET NUMBER_OF_BILLS =:NUM WHERE DENOMINATION =:DEN", {'NUM': new_sum, 'DEN': row[0]})
            cursor.execute("UPDATE ATM_BALANCE SET SUM =:SUM WHERE DENOMINATION =:DEN", {'SUM': new_sum, 'DEN': row[0]})
            conn.commit()
        conn.commit()
        conn.close()
        self.trans.transactions('admin', 'Take money of  the ATM balance', all_sum, self.total_atm())
        return 'The action is completed'

    def quantity_limit(self, banknote):
        '''the function checks whether such amount of banknotes
        is available in the ATM'''

        conn = sqlite3.connect('ATM.db')
        cur = conn.cursor()
        for row in cur.execute("SELECT *FROM ATM_BALANCE"):
            if row[0] == banknote:
                result = row[1]
        conn.commit()
        conn.close()
        return result

    def balance_admin(self):
        '''The function looks at the balance ATM for admin'''

        conn = sqlite3.connect('ATM.db')
        cur = conn.cursor()
        for row in cur.execute("SELECT *FROM ATM_BALANCE"):
            print(row)
        conn.commit()
        conn.close()
        self.trans.transactions('admin', 'Looks at the balance ATM', self.total_atm(), self.total_atm())
        return f' total sum = {self.total_atm()}'

    def top_up_admin(self):
        '''The function tops up  the ATM balance'''

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
            cursor.execute("UPDATE ATM_BALANCE SET NUMBER_OF_BILLS =:BIL WHERE DENOMINATION =:DEN", {'BIL': new_number, 'DEN': row[0]})
            cursor.execute("UPDATE ATM_BALANCE SET SUM =:SUM WHERE DENOMINATION =:DEN", {'SUM': new_sum, 'DEN': row[0]})
        conn.commit()
        conn.close()
        self.trans.transactions('admin', 'Top up the balance', all_sum, self.total_atm())
        return 'The action is completed'

    def red_bal_atm(self, list_banknotes):
        '''The function adjusts ATM balances after withdrawal'''

        for element in list_banknotes:
            conn = sqlite3.connect('ATM.db')
            cur = conn.cursor()
            for row in cur.execute("SELECT *FROM ATM_BALANCE"):
                if row[0] == element[0]:
                    new_number = row[1] - element[1]
                    new_sum = row[0] * new_number
                    cursor = conn.cursor()
                    cursor.execute("UPDATE ATM_BALANCE SET NUMBER_OF_BILLS =:NUM WHERE DENOMINATION =:PAR", {'NUM': new_number, 'PAR': row[0]})
                    cursor.execute("UPDATE ATM_BALANCE SET SUM =:SUM WHERE DENOMINATION =:PAR", {'SUM': new_sum, 'PAR': row[0]})
                    conn.commit()
            conn.commit()
            conn.close()

    def print_banknots(self, list_banknotes):
        '''The function prints bills that have been issued'''

        print('You receive:')
        for banknote in list_banknotes:
            print(f'{banknote[1]} banknotes of {banknote[0]} hryvnias')
        pass

    def trans_history_admin(self):
        ''' Print transaction history for admin'''

        conn = sqlite3.connect('ATM.db')
        cur = conn.cursor()
        for row in cur.execute("SELECT *FROM TRANSACTIONS"):
            print(row)
        conn.commit()
        conn.close()
        self.trans.transactions('admin', 'Print transaction history', self.total_atm(), self.total_atm())
        return 'The action is completed'


class Transactions:
    '''The class creates and stores ATM transactions'''

    def transactions(self, id_user, action, sum_action, final_sum):
        '''The commits transactions'''

        conn = sqlite3.connect('ATM.db')
        cursor = conn.cursor()
        tpans_params = (id_user, f'{datetime.datetime.now()}', action, sum_action, final_sum,)
        cursor.execute("INSERT INTO TRANSACTIONS VALUES (?,?,?,?,?)", tpans_params)
        conn.commit()
        conn.close()
        return


def welcome_menu():
    ''' the function starts'''
    menu = {
        'start': 'For login',
        'reg': 'For registration',
        'exit': 'Exit'
    }
    print('\n************************WELCOME TO OURS ATM *************************************')
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


def admin_menu():
    '''The fuction returns admin_action and choices of action'''
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


def menu():
    '''The fuction returns user_action and choices of action'''

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


def greeting():
    '''the function requests user data returns verified username'''

    attempt = 0
    while attempt < 3:
        username = input('Please, enter your user name:  ')
        user_password = input('Enter your password:  ')
        customer = Customers(username, user_password)
        if customer.verification():
            return customer
        else:
            print("\nOops!!! Username or password is incorrect. Try again... ")
            attempt += 1
    print('The entered data is incorrect, contact the bank')
    return 'Goodbye!!!'


def start_user(user_id):
    '''workflow of user'''

    while True:
        user_action = menu()
        action = Atm(user_id)
        if user_action == 'balance':
            print(f'Your balance is - {action.balance()}')
        if user_action == 'top_up':
            print(action.top_up())
        if user_action == 'pth':
            print(action.trans_history_user())
        if user_action == 'get':
            print(action.receiving())
        if user_action == 'exit':
            return "Goodbye"
        time.sleep(1)
        print('\n Choose the next action or choose ''exit'' to stop')


def start_admin():
    '''workflow of ATM for admin'''

    while True:
        admin_action = admin_menu()
        action = Atm('admin')
        if admin_action == 'balance':
            print(action.balance_admin())
        if admin_action == 'top_up':
            print(action.top_up_admin())
        if admin_action == 'get':
            print(action.take_admin())
        if admin_action == 'pth':
            print(action.trans_history_admin())
        if admin_action == 'exit':
            return
        time.sleep(1)
    print('\n Choose the next action or choose ''exit'' to stop')


def start():
    '''workflow of ATM'''

    while True:
        next_step = welcome_menu()
        if next_step == 'exit':
            return "Good bye"
        if next_step == 'reg':
            while True:
                username = input('Please, enter your username:  ')
                user_password = input('Please, enter your password:  ')
                customer = Customers(username, user_password)
                if customer.new_user():
                    customer.add_new_user()
                    break
        if next_step == 'start':
            customer = greeting()
            print(f'Hello {customer.username}')
            if customer.username == 'admin':
                start_admin()
            else:
                user_id = customer.return_id()
                start_user(user_id)


if __name__ == "__main__":

    print(start())
