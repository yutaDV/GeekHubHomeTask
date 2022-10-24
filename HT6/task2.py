'''НT2.Створіть функцію для валідації пари ім'я/пароль за наступними правилами:
   - ім'я повинно бути не меншим за 3 символа і не більшим за 50;
   - пароль повинен бути не меншим за 8 символів і повинен мати хоча б одну
   цифру;
   - якесь власне додаткове правило :)- ім'я не має бути частиною паролю
   Якщо якийсь із параметрів не відповідає вимогам - породити виключення
    із відповідним текстом.'''


class NonValidUserError(Exception):
    pass


def validation(username, password):
    '''The function checks the correct name and password'''

    password_digit = 0
    for letter in password:
        if letter.isdigit():
            password_digit += 1
    if len(username) < 3:
        raise NonValidUserError("Your name is too short ")
    elif len(username) > 50:
        raise NonValidUserError("Your name is too long ")
    elif len(password) < 8:
        raise NonValidUserError("Your password is too short ")
    if password_digit == 0:
        raise NonValidUserError("password must have at least one digit ")
    elif username in password:
        raise NonValidUserError("The password cannot contain a name ")
    return True


username = input('Please, enter your username:  ')
password = input('Please, enter your password:  ')
try:
    print(validation(username, password))
except NonValidUserError as e:
    print(f'Goodbye {e}')
