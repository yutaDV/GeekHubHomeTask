'''HT 13 2. Створити клас Matrix, який буде мати наступний функціонал:
1. __init__ - вводиться кількість стовпців і кількість рядків
2. fill() - заповнить створений масив числами - по порядку. Наприклад:
+────+────+
| 1  | 2  |
+────+────+
| 3  | 4  |
+────+────+
| 5  | 6  |
+────+────+
3. print_out() - виведе створений масив (якщо він ще не заповнений даними
- вивести нулі
4. transpose() - перевертає створений масив. Тобто, якщо взяти попередню
таблицю, результат буде
+────+────+────+
| 1  | 3  | 5  |
+────+────+────+
| 2  | 4  | 6  |
+────+────+────+
P.S. Всякі там Пандас/Нампай не використовувати - тільки хардкор ;)
P.P.S. Вивід не обов’язково оформлювати у вигляді таблиці - головне,
щоб було видно, що це окремі стовпці / рядки'''


class Matrix:

    def __init__(self, columns, rows):
        self.columns = columns
        self.rows = rows
        self.matrix = self.create_matrix()

    def create_matrix(self):

        self.matrix = []
        element = None
        for r in range(self.rows):
            row = []
            for c in range(self.columns):
                row.append(element)
            self.matrix.append(row)
        return self.matrix

    def fill(self):

        self.matrix = []
        count = 1
        for r in range(self.rows):
            row = []
            for c in range(self.columns):
                row.append(count)
                count += 1
            self.matrix.append(row)
        return self.matrix

    def print_out(self):

        result = f''
        for r in range(self.rows):
            for c in range(self.columns):
                if self.matrix[r][c] is None:
                    self.matrix[r][c] = 0
                result += f' {self.matrix[r][c]}  '
            result += f'\n'
        return result

    def transpose(self):

        bufer_matrix = self.matrix
        bufer = self.rows
        self.rows = self.columns
        self.columns = bufer
        self.matrix = []
        for r in range(self.rows):
            row = []
            for c in range(self.columns):
                row.append(bufer_matrix[c][r])
            self.matrix.append(row)
        return self.matrix


matrix = Matrix(2, 3)
print(matrix.print_out())
print(matrix.fill())
print(matrix.print_out())
print(matrix.transpose())
print(matrix.print_out())
