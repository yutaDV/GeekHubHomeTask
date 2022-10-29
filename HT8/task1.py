'''НT8.1.   Створити програму-емулятор світлофора для авто і пішоходів.
Після запуска програми на екран виводиться в лівій половині - колір
автомобільного, а в правій - пішохідного світлофора. Кожну 1 секунду
виводиться поточні кольори. Через декілька ітерацій - відбувається
зміна кольорів - логіка така сама як і в звичайних світлофорах
(пішоходам зелений тільки коли автомобілям червоний).
   Приблизний результат роботи наступний:
      Red        Green
      Red        Green
      Red        Green
      Red        Green
      Yellow     Red
      Yellow     Red
      Green      Red
      Green      Red
      Green      Red
      Green      Red
      Yellow     Red
      Yellow     Red
      Red        Green '''

import time

cars_light = [
    'Red', 'Red', 'Red', 'Red',
    'Yellow', 'Yellow',
    'Green', 'Green', 'Green', 'Green'
]
while True:
    for car_light in cars_light:
        if car_light == "Red":
            pedestrian_light = 'Green'
        else:
            pedestrian_light = "Red"
        time.sleep(1)
        print(car_light.ljust(50), pedestrian_light)
        