'''НT7.2.  Запишіть в один рядок генератор списку (числа в діапазоні
від 0 до 100 не включно), сума цифр кожного елемент якого буде дорівнювати 10.
Результат: [19, 28, 37, 46, 55, 64, 73, 82, 91].'''

result = [x for x in range(100) if x // 10 + x % 10 == 10]
print(result)
