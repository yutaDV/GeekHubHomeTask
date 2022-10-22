'''НT2.Створіть функцію для валідації пари ім'я/пароль за наступними правилами:
   - ім'я повинно бути не меншим за 3 символа і не більшим за 50;
   - пароль повинен бути не меншим за 8 символів і повинен мати хоча б одну
   цифру;
   - якесь власне додаткове правило :)- ім'я не має бути частиною паролю
   Якщо якийсь із параметрів не відповідає вимогам - породити виключення
    із відповідним текстом.'''


def validation(username, password):
    '''The function checks the correct name and password'''

    if len(username) < 3:
        raise Exception("Your name is too short ")
    elif len(username) > 50:
        raise Exception("Your name is too long ")
    i = 0
    for letter in password:
        if letter.isdigit():
            i += 1
    if i == 0:
        raise Exception("password must have at least one digit ")
    elif username in password:
        raise Exception("The password cannot contain a name ")
    return True


username = input('Please, enter your username:  ')
password = input('Please, enter your password:  ')
try:
    print(validation(username, password))
except Exception as e:
    print(f'Goodbye {e}')