'''НT3. На основі попередньої функції (скопіюйте кусок коду)
 створити наступний скрипт:
   а) створити список із парами ім'я/пароль різноманітних видів
    (орієнтуйтесь по правилам своєї функції) - як валідні, так і ні;
   б) створити цикл, який пройдеться по цьому циклу
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


zoo_data = [
    {'cat': 'cat&mouse2'}, {'hare': '4carrots for breacfest'},
    {'fox': 'hare'}, {'wolf': 'fox'}, {'bear': 'honey'},
    {'fox': 'hare'}, {'wolf': 'fox'}, {'bear': 'honey'},
    {'foxcatmousefoxharewolfoxbearhoneyfoxcatmousefoxhare': '1234gkfl'}
]
username = input('Please, enter your username:  ')
password = input('Please, enter your password:  ')
try:
    print(validation(username, password))
except Exception as e:
    print(f'Goodbye {e}')
