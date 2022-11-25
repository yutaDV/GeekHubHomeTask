'''HT 12 TASK  #2. Створіть за допомогою класів та продемонструйте свою
реалізацію шкільної бібліотеки (включіть фантазію). Наприклад вона може
містити класи Person, Teacher, Student, Book, Shelf, Author, Category і.т.д.
Можна робити по прикладу банкомату з меню, базою даних і т.д.'''

import sqlite3
import time


class Persons:
    token = 'r_c'
    """Library topic user class.

    Objects of the class are clients that can use the library.
    Attributes of the class name, ID, age, token (divides users into
    the categories r_c - children, r - adults, vip - VIP clients,
    admin -librarian)"""

    def __init__(self, name, age):
        """The constructor of the class, ID is generated automatically
        as a serial number, the token is generated according to the age
        of the user, only the librarian can change the token"""
        self.user_id = self.user_id()
        self.name = name
        self.age = age

    def create_reader(self):
        """The function adjusts the token according to
        the age of the user at the time of creation."""

        if self.is_adult():
            self.token = 'r'

    def add_new_reader(self):
        """The function adds a new user to BD"""

        if self.is_adult():
            self.token = 'r'
        conn = sqlite3.connect('LIBRARY.db')
        cursor = conn.cursor()
        params = (self.user_id, self.name, self.age, self.token)
        cursor.execute("INSERT INTO PERSONS VALUES (?,?,?,?)", params)
        conn.commit()
        conn.close()
        print('Your registration was successful!!')
        return

    def is_adult(self):
        """The function checks whether the user is of legal age."""

        if self.age >= 21:
            return True
        return False

    def user_id(self):
        """The function returns  the next ID"""

        conn = sqlite3.connect('LIBRARY.db')
        cur = conn.cursor()
        user_id = len(cur.execute("SELECT * FROM PERSONS").fetchall()) + 1
        conn.commit()
        conn.close()
        return user_id

    def acces_to_read(self):
        """The function returns a list of reading
        materials for the user."""

        if self.token == 'r_c':
            return ['r_c']
        if self.token == 'r':
            return ['r', 'r_c']
        if self.token == 'vip' or self.token == 'admin':
            return ['r', 'r_c', 'vip']

    def return_reader(self, name):
        """The function adjusts user attributes
        when accessing the library."""

        try:
            conn = sqlite3.connect('LIBRARY.db')
            cur = conn.cursor()
            for row in cur.execute("SELECT * FROM PERSONS"):
                if row[1] == name:
                    self.id = row[0]
                    self.age = row[2]
                    self.token = row[3]
            conn.commit()
            conn.close()
        except:
            return False
        return True


class Librarian(Persons):
    """The Librarian class is a subclass of Persons"""
    password = 'admin'
    token = 'admin'

    def __init__(self, name, age):
        super().__init__(name, age)

    def validation_password(self):
        """The function will check the librarian's password"""

        password = input("Input your password: ")
        if password == self.password:
            return True


class Literature:
    """The class of creating objects of literature

    Attributes include book title, author, genre, date of creation,
    number of copies, and token"""

    def __init__(self, name, author, genre, date_of_creat, number, token):
        """The constructor of the ID class is formed automatically according
        to the serial number of the book in the database."""
        self.liter_id = self.liter_id()
        self.name = name
        self.author = author
        self.genre = genre
        self.date_of_creat = date_of_creat
        self.number = number
        self.token = token

    def __str__(self):
        return f" Name - {self.name}, author - {self.author}, date of creation {self.date_of_creat}"

    def liter_id(self):
        """The function returns  the book ID"""

        conn = sqlite3.connect('LIBRARY.db')
        cur = conn.cursor()
        liter_id = len(cur.execute("SELECT * FROM Literature").fetchall()) + 1
        conn.commit()
        conn.close()
        return liter_id

    def add_new_literatur(self):
        "The function adds a new book to the database"""

        conn = sqlite3.connect('LIBRARY.db')
        cursor = conn.cursor()
        params = (self.liter_id, self.name, self.author, self.date_of_creat, self.genre, self.number, self.token)
        cursor.execute("INSERT INTO Literature VALUES (?,?,?,?,?,?,?)", params)
        conn.commit()
        conn.close()
        print('You did it!')
        return


class ChildrenBook(Literature):
    """The subclass of the literature class. Additional
    functions and attributes are still under development))"""
    token = 'r_c'
    pass


class VipBook(Literature):
    """The subclass of the literature class. Additional
    functions and attributes are still under development))"""
    token = 'vip'
    pass


class Action:
    """Library action class. The class contains
     user and book interaction functions."""

    def __init__(self, user_id=None):
        self.user_id = user_id

    def verification(self):
        '''the function verifies the correctness of the entered user
         name'''

        name = input('Please, enter your name and surname:  ')
        conn = sqlite3.connect('LIBRARY.db')
        cur = conn.cursor()
        try:
            cur.execute("""SELECT * FROM PERSONS WHERE NAME =:NAME""",
                        {'NAME': name})
            if cur.fetchone()[1] == self.user_password:
                self.user_id = cur.fetchone()[0]
                conn.commit()
                conn.close()
                return self.user_id
        except:
            return 'Sorry You are not our customer/ Try agfin'

    def look_books(self, acces_list):
        """ The function prints a list of references for the user."""

        conn = sqlite3.connect('LIBRARY.db')
        cur = conn.cursor()
        for row in cur.execute("SELECT * FROM Literature"):
            if row[6] in acces_list and row[5] > 0:
                print(f'Book: "{row[1]}", author: {row[2]}, genre: {row[4]}')
                time.sleep(1)
        conn.commit()
        conn.close()
        return


class ActionAdmin(Action):
    """a subclass of the action class, describes additional actions
    for the librarian, these actions are not valid for readers"""
    user_id = 'admin'

    def create_reader(self):
        """The function creates a librarian reader"""

        name = input('Enter the readers name and surname: ')
        while True:
            try:
                age = int(input('Enter readers age:  '))
            except:
                print('The answer is not correct, enter readers age')
            else:
                if 5 < age < 120:
                    break
                else:
                    print('The age is not correct. Try again')
        return Persons(name, age)

    def chose_token(self):
        """The function selects a token"""

        token_dict = {
            'r_c': 'registration of ordinary reader',
            'r': 'registration of ordinary reader',
            'vip': 'registration of vip reader',
            'admin': 'registration of librarian'
        }
        while True: 
            print('Chose the token for new user')
            for key, value in token_dict.items():
                print(f'{key} for {value}')
            token = input('input token :')
            if token in token_dict.keys():
                break
            else:
                print('The token is not correct. Try again')
        return token

    def chenge_token(self, id_reader):
        """The function changes the token for the current user"""

        token = self.chose_token()
        conn = sqlite3.connect('LIBRARY.db')
        cur = conn.cursor()
        cur.execute("""UPDATE PERSONS
                    SET Token =:Token WHERE ID_READER =:ID""",
                    {'Token': token, 'ID': id_reader})
        conn.commit()
        conn.close()
        return f'The action is completed. new token {token}'

    def create_literature(self):
        """The function creates objects of literature"""

        name = input('Enter a  name of the book: ')
        author = input('Enter a  author of the book: ')
        date_of_creat = input('Enter a date of creat the book: ')
        genre = input('Enter a  genre of the book: ')
        while True:
            try:
                number = int(input('Enter a number of books:  '))
            except:
                print('The answer is not correct, enter a number')
            else:
                if number > 0:
                    break
                else:
                    print('The value is not correct. Try again')
        while True:
            token = input('Enter a token (r, r_c, vip):  ')
            if token in ['r', 'r_c', 'vip']:
                break
            else:
                print('The value is not correct. Try again')
        return Literature(name, author, genre, date_of_creat, number, token)

    def look_books(self):
        """ the function of viewing a complete list of literature"""

        conn = sqlite3.connect('LIBRARY.db')
        cur = conn.cursor()
        for row in cur.execute("SELECT * FROM Literature"):
            print(f'Book: "{row[1]}", author: {row[2]}, date: {row[3]}, genre: {row[4]}, number: {row[5]}, token: date: {row[6]}')
        conn.commit()
        conn.close()
        return

    def look_readers(self):
        """The  function of viewing the list of readers"""

        conn = sqlite3.connect('LIBRARY.db')
        cur = conn.cursor()
        for row in cur.execute("SELECT * FROM PERSONS"):
            print(f'Reader: "{row[1]}", age: {row[2]}, token: {row[3]}')
        conn.commit()
        conn.close()
        return


def chek_name(name):
    """The function checks a reader's name"""

    conn = sqlite3.connect('LIBRARY.db')
    cur = conn.cursor()
    try:
        for row in cur.execute("SELECT NAME FROM PERSONS"):
            if row[0] == name:
                conn.commit()
                conn.close()
                return True
    except:
        return False
    else:
        return False


def librarian_menu():
    """ the librarian menu"""

    menu = {
        'c_r': 'For creating a new readers',
        'c_t': 'For chenging the readers token',
        'c_l': 'For creating a new literature',
        'r_v': 'For readers to view',
        'l_v': 'For literature review',
        'exit': 'Exit'
    }

    for key, value in menu.items():
        print(f'{key} for {value}')
    while True:
        time.sleep(1)
        next_step = input('\nEnter one of the actions listed above:')
        if next_step in menu:
            return next_step
        print('Oops!!! the action is incorrect. Try again...')


def start_librarian():
    """workflow of library for librarian"""

    library = Librarian('admin', None)
    if library.validation_password():
        while True:
            next_step = librarian_menu()
            action = ActionAdmin('admin')
            if next_step == 'c_r':
                reader = action.create_reader()
                reader.add_new_reader()
            if next_step == 'c_t':
                user_id = int(input('Input id_reader:'))
                print(action.chenge_token(user_id))
            if next_step == 'c_l':
                book = action.create_literature()
                print(f'You have added a book - {book}')
                book.add_new_literatur()
            if next_step == 'r_v':
                action.look_readers()
            if next_step == 'l_v':
                action.look_books()
            if next_step == 'exit':
                return
            time.sleep(1)
            print('\n Choose the next action or choose ''exit'' to stop')
    else:
        return ('Oops!!! the pasword is incorrect. Goodbuy...')


def start():
    """workflow of Library"""

    print('\n************************WELCOME TO OUR LIBRARY *************************************')
    while True:
        answer = input('\nAre you a customer of our library?(YES/NO)  - ')
        if answer.lower() == "no":
            while True:
                username = input('Please, enter your name and surname:  ')
                try:
                    age = int(input('Please, enter your age:  '))
                except:
                    print('1 The answer is not correct, enter your age')
                else:
                    if 5 < age < 120:
                        reader = Persons(username, age)
                        reader.create_reader()
                        reader.add_new_reader()
                        print('You dad it. You are customer!!!')
                        break
                    elif age < 6:
                        print('Hello, you are still too young? you can visit the library with yout parents')
                        break
                    else:
                        print('The answer is not correct. Try again')
        if answer.lower() == "yes":
            name = input('Please, enter your name and surname:  ')
            if name == 'admin':
                start_librarian()
            else:
                if chek_name(name):
                    reader = Persons(name, None)
                    reader.return_reader(name)
                    print(f'Hello, {reader.name}, you can to read this books:')
                    acces = reader.acces_to_read()
                    next_step = Action()
                    next_step.look_books(acces)
                else:
                    print('You are not our customer? but You can registration')


if __name__ == "__main__":

    print(start())
