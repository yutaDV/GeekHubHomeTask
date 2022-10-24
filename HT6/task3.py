'''НT3. На основі попередньої функції (скопіюйте кусок коду)
 створити наступний скрипт:
   а) створити список із парами ім'я/пароль різноманітних видів
    (орієнтуйтесь по правилам своєї функції) - як валідні, так і ні;
   б) створити цикл, який пройдеться по цьому списку
   і, користуючись валідатором, перевірить ці дані і
   надрукує для кожної пари значень відповідне повідомлення, наприклад:
      Name: vasya
      Password: wasd
      Status: password must have at least one digit
      -----
      Name: vasya
      Password: vasyapupkin2000
      Status: OK
   P.S. Не забудьте використати блок try/except ;)'''


class NonValidUserError(Exception):
    pass


def validation(username, password):
    '''The function checks the correct name and password'''

    if len(username) < 3:
        raise NonValidUserError("Your name is too short ")
    elif len(username) > 50:
        raise NonValidUserError("Your name is too long ")
    elif len(password) < 8:
        raise NonValidUserError("Your password is too short ")
    i = 0
    for letter in password:
        if letter.isdigit():
            i += 1
    if i == 0:
        raise NonValidUserError("password must have at least one digit ")
    elif username in password:
        raise NonValidUserError("The password cannot contain a name ")
    return True


zoo_data = [
    {'cat': 'cat&mouse2'}, {'hare': '4carrots_for_breacfest'},
    {'fox': 'hare'}, {'wolf': 'fox256fo'}, {'be': 'honey12568'},
    {'fox': 'like4hare'}, {'wolf': 'fox'}, {'dog': 'frendnumber1'},
    {'foxcatmousefoxharewolfoxbearhoneyfoxcatmousefoxhare': '1234gkfl'}
]

for element in zoo_data:
    for key, value in element.items():
        try:
            validation(key, value)
        except NonValidUserError as e:
            print(f'Name:{key}\nPassword:{value}\nStatus:{e}\n   -----')
        else:
            print(f'Name:{key}\nPassword:{value}\nStatus:OK\n   -----')
