'''HT 11 TASK  #2. Створити клас Person, в якому буде присутнім метод 
    __init__ який буде приймати якісь аргументи, які зберігатиме
    в відповідні змінні.
    - Методи, які повинні бути в класі Person - show_age, print_name,
       show_all_information
    - Створіть 2 екземпляри класу Person та в кожному з екземплярів
      створіть атрибут profession (його не має інсувати під час ініціалізації
       в самому класі) та виведіть його на екран (прінтоніть)'''


class Person:

    def __init__(self, name, age, gender, pets):
        self.name = name
        self.age = age
        self.gender = gender
        self.pets = pets

    def show_age(self):
        return self.age

    def print_name(self):
        print(self.age)

    def is_aduit(self, age):
        if age >= 21:
            return True
        return False

    def show_all_information(self):
        return self.name, self.age, self.gender, self.pets


p1 = Person("John", 23, 'men', 'cat')
p2 = Person("Max", 36, 'men', 'dog')
p1.profession = 'doctor'
p2.profession = 'teacher'

print(p1.name)
print(p2.is_aduit(p2.age))
print(p1.profession)
print(p2.profession)
print(p1.show_age())
print(p1.is_aduit(p1.age))
print(p2.show_all_information())
