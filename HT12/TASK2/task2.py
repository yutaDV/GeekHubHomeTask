'''HT 12 TASK  #2. Створіть за допомогою класів та продемонструйте свою
реалізацію шкільної бібліотеки (включіть фантазію). Наприклад вона може
містити класи Person, Teacher, Student, Book, Shelf, Author, Category і.т.д.
Можна робити по прикладу банкомату з меню, базою даних і т.д.'''


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
