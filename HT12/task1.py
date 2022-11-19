''' HT 12 Напишіть програму, де клас «геометричні фігури» (Figure) 
містить властивість color з початковим значенням white і метод для
зміни кольору фігури, а його підкласи «овал» (Oval) і «квадрат»
(Square) містять методи _init_ для завдання початкових розмірів
об'єктів при їх створенні.'''

import math


class Figure:
    """ Батьківський клас для фігур які за замовчуванням є білими

    атрибутами класу є колів фігур який за замовчуванням є білий
    функція color_change довзволяє зінити колів фігури на вибір користувача"""
    color = 'white'

    def color_change(self):
        """Функція зміни кольору фігури на вибір користувача"""
        color_dict = {
            1: 'black', 2: 'white', 3: 'blue', 4: 'yellow',
            5: 'green', 6: 'red', 7: 'purple', 8: 'gray'
        }
        new_color = None
        print('If you want to change a color of the figure chose a new color')
        for key, value in color_dict.items():
            print(f'Input {key} for {value}')
        while True:
            try:
                new_color = int(input('Input a number of the color: '))
            except:
                print('Incorrect data, enter a number from 1 to 8. Try again')
            else:
                if 0 < new_color < 9:
                    break
                else:
                    print('Enter a number from 1 to 8. Try again')
        self.color = color_dict.get(new_color)
        return


class Oval(Figure):
    """Клас створення овалу за його параметрами"""

    def __init__(self, big_radius, small_radius):
        self.big_radius = big_radius
        self.small_radius = small_radius

    def perimetr(self):
        big = self.big_radius
        small = self.small_radius
        return 4 * ((math.pi * big * small + (big + small) ** 2) / (big + small))

    def area(self):
        return self.big_radius * self.small_radius * math.pi


class Square(Figure):
    """Клас створення квадрату за його параметрами

    функції класу розраховують периметр та площу квадрату"""

    def __init__(self, side):
        self.side = side

    def perimetr(self):
        return self.side * 4

    def area(self):
        return self.side ** 2


set_1 = Square(9)
print(set_1.color)
set_2 = Oval(10, 5)
set_1.color_change()
print(set_1.color)
print(set_2.perimetr())
print(set_2.area())
print(set_2.color)
print(set_1.perimetr())
print(set_1.area())
