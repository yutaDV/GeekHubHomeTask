'''HT 11 TASK  #2. Створити клас Person, в якому буде присутнім метод 
    __init__ який буде приймати якісь аргументи, які зберігатиме
    в відповідні змінні.
    - Методи, які повинні бути в класі Person - show_age, print_name,
       show_all_information'''


class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)
