'''НT11. 3   Банкомат 4.0: переробіть программу з функціонального підходу
програмування на використання класів. Додайте шанс 10% отримати бонус на
 баланс при створенні нового користувача.'''

import sqlite3
import datetime
import time
import random


class Customers():

    def __init__(self, id, username, user_password, user_balanse, admin_token):
        self.id = id
        self.username = username
        self.user_password = user_password
        self.user_balanse = user_balanse
        self.admin_token = False

    def verification(self, username, user_password):
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

    def greeting(self):
        '''the function requests user data returns verified username
        // вітання користувача'''

        attempt = 0
        while attempt < 3:
            username = input('Please, enter your user name:  ')
            user_password = input('Enter your password:  ')
            if self.verification(self, username, user_password):
                return username
            else:
                print("\nOops!!! Username or password is incorrect. Try again... ")
                attempt += 1
        print('The entered data is incorrect, contact the bank')
        return 'Goodbye!!!'
    
    def validation_password(self, username, user_password):
        '''The function checks the correct name and password for new user?????'''

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
        '''the function draws 1,000 hryvnias to the balance for a new user//
        функція розігрує 1000 гривень на баланс для нового користувача'''

        print("\nYou have the honor of winning 1000 hryvnias for your balance!")
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
        ''' The function registrations of new user// рестрація нового
         користувача первірка паролю та імені на валідність'''
        while True:
            username = input('Please, enter your username:  ')
            user_password = input('Please, enter your password:  ')
            if self.validation_password(self, username, user_password):
                return self.username, self.user_password
            print("Oops!!! The answer is incorrect. Try again...")
        return self.username, self.user_password

    def add_new_user(self, username, user_password):
        ''' The function adds a new user// функція
        додає дані нового користувача до БД'''
        if self.bonus_draw():
            new_balance = 1000
        else:
            new_balance = 0
        conn = sqlite3.connect('ATM.db')
        cursor = conn.cursor()
        sum_id = 0
        for row in cursor.execute("SELECT *FROM USERS"):
            sum_id += 1
        params = (sum_id + 1, self.username, self.user_password, new_balance, self.admin_token)
        cursor.execute("INSERT INTO USERS VALUES (?,?,?,?,?)", params)
        conn.commit()
        conn.close()
        print('Your registration was successful!!')
        return True

    def return_id(self, username):
        '''The function returns  the user_ID'''

        conn = sqlite3.connect('ATM.db')
        cur = conn.cursor()
        cur.execute("SELECT * FROM USERS WHERE NAME =:NAME", {'NAME':self.username})
        user_id = cur.fetchone()[0]
        conn.close()
        return user_id

    


class Atm():

    def __init__(self, id, user_balanse=None):
        self.id = id
        self.user_balanse = None

    def verification_user_sum(self, id=None):
            '''the function checks whether the entered number is a float and return
            the number// перевірка введеної суми'''

            while True:
                try:
                    try_sum = float(input('Enter the amount: '))
                except:
                    print("Oops!!! The amount is incorrect. You amount must be a number. Try again...")
                else:
                    if try_sum >= self.min_bank_atm():
                        if try_sum // 10 == 0:
                            user_sum = try_sum
                            return (user_sum, 2)
                        else:
                            user_sum = try_sum - try_sum % 10
                            print(f'Amount to be processed {user_sum}the rest {try_sum % 10} was returned')
                            return round(user_sum, 2)
                    else:
                        print(f"Oops!!! The amount is incorrect. You amount must be greater than {self.min_bank_atm()}. Try again...")

    def balance(self):
        '''The function looks at the balance// функція перевірки балансу'''

        id = self.id
        conn = sqlite3.connect('ATM.db')
        cur = conn.cursor()
        cur.execute("SELECT * FROM USERS WHERE ID =:ID", {'ID': id})
        result = cur.fetchone()[3]
        conn.commit()
        conn.close()
        Tramsactions.tramsactions(Tramsactions, id, 'Looks at the balance', result, result)
        return f'Your belance:{result}'

    def top_up(self):
        '''The function tops up  the user balance// поповнення балансу'''
        
        id = self.id
        conn = sqlite3.connect('ATM.db')
        cur = conn.cursor()
        user_sum = self.verification_user_sum()
        cur.execute("SELECT * FROM USERS WHERE ID =:ID", {'ID':id})
        user_balanse = cur.fetchone()[3] + user_sum
        cur.execute("UPDATE USERS SET BALANCE =:BAL WHERE ID =:ID", {'BAL':user_balanse, 'ID':id})
        conn.commit()
        conn.close()
        Tramsactions.tramsactions(Tramsactions, id, 'Top up the balance', user_sum, user_balanse)
        return 'The action is completed'

    def perfect_set(self, user_sum):
        '''ідеальний набір банкнот для видачі  від бульшого до меншого
         з урахуванням кільклсті банкнот'''

        bancnots = self.banknotes_in_atm()
        result = []
        for par in bancnots:
            amount = user_sum // par
            amount_atm = self.quantity_limit(par)
            if amount_atm >= amount > 0:
                result.append((par, amount))
                user_sum = user_sum % par
            if amount > 0 and amount > amount_atm:
                result.append((par, amount_atm))
                user_sum -= (par * amount_atm)
            if user_sum == 0:
                return result, user_sum
        return result, user_sum

    def second_set(self, user_sum):
        '''якщо перший варіант провалився то резервуємо одну наманшу купюру і
         перевіряємо чи все ок, якщо ні то ше мінус 1 (відмінусовані купюри
        додати вкінці, якщо такого не трапилось то Nane)'''

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
        '''підбір кількості банкнот для зняття, шляхом відмови від найбільшої'''

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
        '''The function receis money  the user balance//зняття коштів'''

        id = self.id
        conn = sqlite3.connect('ATM.db')
        cur = conn.cursor()
        cur.execute("SELECT * FROM USERS WHERE ID =:ID", {'ID': id})
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
            cur.execute("UPDATE USERS SET BALANCE =:BALANCE WHERE ID =:ID", {'BALANCE':new_balance,'ID':self.id})
            conn.commit()
            conn.close()
            print(f'')
            self.red_bal_atm(super_set)
            self.print_banknots(super_set)
            Tramsactions.tramsactions(Tramsactions, id, 'Top up the balance', user_sum, new_balance)
            return 'The action is completed'

    def trans_history_user(self):
        ''' Print transaction history for user'''

        id = self.id
        conn = sqlite3.connect('ATM.db')
        cur = conn.cursor()
        for row in cur.execute("SELECT *FROM TRANSACTIONS"):
            if self.id == row[0]:
                print(f'Date - {row[1]}, action - {row[2]},sum {row[3]}, final_sum {row[4]}')
        conn.commit()
        conn.close()
        Tramsactions.tramsactions(Tramsactions, id, 'Print transaction history', None, None)
        return 'The action is completed'

    def start_user(self, username):
        '''workflow of user'''

        user_id = return_id(self.username)
        while True:
            if user_id:
                user_action = Menu.menu()
                if user_action == 'balance':
                    print(self.balance(user_id))
                if user_action == 'top_up':
                    print(self.top_up(user_id))
                if user_action == 'pth':
                    print(self.trans_history_user(user_id))
                if user_action == 'get':
                    print(self.receiving(user_id))
                if user_action == 'exit':
                    return "Goodbye"
                time.sleep(1)
                print('\n Choose the next action or choose ''exit'' to stop')

    def banknotes_in_atm(self, id=None):
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

    def min_bank_atm(self, id=None):
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

    def total_atm(self, id=None):
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

    def take_admin(self, id='admin'):
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
        Tramsactions.tramsactions(Tramsactions,'admin', 'Take money of  the ATM balance', all_sum, self.total_atm())
        return 'The action is completed'

    def quantity_limit(self, par):
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

    def balance_admin(self, id='admin'):
        '''The function looks at the balance ATM for admin//
        функція перевірки балансу ATM'''

        conn = sqlite3.connect('ATM.db')
        cur = conn.cursor()
        for row in cur.execute("SELECT *FROM ATM_BALANCE"):
            print(row)
        conn.commit()
        conn.close()
        Tramsactions.tramsactions(Tramsactions, 'admin', 'Looks at the balance ATM', self.total_atm(), self.total_atm())
        return f' total sum = {self.total_atm()}'

    def top_up_admin(self, id='admin'):
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
        Tramsactions.tramsactions(Tramsactions, 'admin', 'Top up the balance', all_sum, self.total_atm())
        return 'The action is completed'

    def red_bal_atm(self, list_pars, id=None):
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

    def print_banknots(self, list_pars, id=None):
        '''друк банкнот які було видано'''

        print('You receive:')
        for par in list_pars:
            print(f'{par[1]} banknotes of {par[0]} hryvnias')
        pass

    def trans_history_admin(self, id='admin'):
        ''' Print transaction history for admin'''

        conn = sqlite3.connect('ATM.db')
        cur = conn.cursor()
        for row in cur.execute("SELECT *FROM TRANSACTIONS"):
            print(row)
        conn.commit()
        conn.close()
        Tramsactions.tramsactions(Tramsactions, 'admin', 'Print transaction history', self.total_atm(), self.total_atm())
        return 'The action is completed'


class Menu():
    """Обєктами класу є вигляд інтерфейсу АТМ"""

    def welcome_menu():
        ''' the function starts//'''
        menu = {
            'start': 'For login',
            'reg': 'For registration',
            'exit': 'Exit'
        }
        print('\n*****це якась діч, щось в цій темі я роблю і розумію не так буду ще читати, бо воно все не працює *********')
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



    def start_admin(self):
        '''workflow of ATM for admin'''

        while True:
            admin_action = Menu.admin_menu()
            if admin_action == 'balance':
                print(self.balance_admin())
            if admin_action == 'top_up':
                print(self.top_up_admin())
            if admin_action == 'get':
                print(self.take_admin())
            if admin_action == 'pth':
                print(self.trans_history_admin())
            if admin_action == 'exit':
                return
            time.sleep(1)
        print('\n Choose the next action or choose ''exit'' to stop')


class Tramsactions():
    def __init__(self, id_user, action, sum_action, final_sum):
        self.id_user = id_user
        self.action = action
        self.sum_action = sum_action
        self.final_sum = sum_action

    def tramsactions(self, id_user, action, sum_action, final_sum):
        '''The commits transactions'''

        conn = sqlite3.connect('ATM.db')
        cursor = conn.cursor()
        tpans_params = (id_user, f'{datetime.datetime.now()}', action, sum_action, final_sum,)
        cursor.execute("INSERT INTO TRANSACTIONS VALUES (?,?,?,?,?)", tpans_params)
        conn.commit()
        conn.close()
        return

def start():
    '''workflow of ATM'''

    while True:
        next_step = Menu.welcome_menu()
        if next_step == 'exit':
            return "Good bye"
        if next_step == 'reg':
            username, password = Customers.new_user(Customers)
            Customers.add_new_user(username, password)
        if next_step == 'start':
            username = Customers.greeting(Customers)
            if username == 'admin':
                Menu.start_admin()
            else:
                Customers.start_user(username)


if __name__ == "__main__":
    
    atm = Atm(7)
    print(atm.top_up_admin())
