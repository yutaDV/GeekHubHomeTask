''' HT 13.1 стовріть клас Car, який буде мати власивіть year (рік випуску).
  Додайте всі необхідні методи до класу щоб можна було виконувати порівняння
  car 1 > car 2. Також операція car 1 - car 2 повинна повернути
  різницю між роками випуску'''


class Car:
    """ клас обєктами якого є автомобілі та їх характеристики

    атрибутами класу є  модель, колір та рік випуску автомобіля"""

    def __init__(self, model, color, year):
        self.model = model
        self.color = color
        self.year = year

    def __str__(self):
        return f"Car model - {self.model}, color - {self.color}, year of production -{self.year}"

    def __lt__(self, other):
        return self.year < other.year

    def __le__(self, other):
        return self.year <= other.year

    def __eq__(self, other):
        return self.year == other.year

    def __ne__(self, other):
        return self.year != other.year

    def __gt__(self, other):
        return self.year > other.year

    def __ge__(self, other):
        return self.year >= other.year

    def __sub__(self, other):
        return self.year - other.year


car_1 = Car('volvo', 'white', 1990)
car_2 = Car('volvo', 'white', 1985)
car_3 = Car('volvo', 'white', 2000)

print(car_1)
print(car_1 - car_2)
print(car_1 - car_3)
print(car_1 > car_2)
print(car_1 >= car_3)
print(car_1 <= car_2)
print(car_1 != car_3)
