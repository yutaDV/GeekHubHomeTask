''' HT 11 TASK  #1  Створити клас Calc, який буде мати атребут last_result
    та 4 методи. Методи повинні виконувати математичні операції
    з 2-ма числами, а саме додавання, віднімання, множення, ділення.
    - Якщо під час створення екземпляру класу звернутися до атрибута
      last_result він повинен повернути пусте значення.
    - Якщо використати один з методів - last_result повинен повернути
    результат виконання ПОПЕРЕДНЬОГО методу.
    Example:
    last_result --> None
    1 + 1
    last_result --> None
    2 * 3
    last_result --> 2
    3 * 4
    last_result --> 6
    ...
- Додати документування в клас (можете почитати цю статтю:'''


class MathOper:
    result = None
    last_result = None
    """The class performs arithmetic operations with two numbers +, -, /, *

    The class includes four objects, two of which have int or float
    which are the arguments of mathematical operations, the other two
    are the default - None that store the current and previous result """

    def add(self, number_1, number_2):
        """ a simple function adds two numbers"""
        self.last_result = self.result
        self.result = number_1 + number_2
        return self.result

    def subtraction(self, number_1, number_2):
        """ a simple function subtracts the second number from the first"""
        self.last_result = self.result
        self.result = number_1 - number_2
        return self.result

    def multi(self, number_1, number_2):
        """a simple function multiplies two numbers"""
        self.last_result = self.result
        self.result = number_1 * number_2
        return self.result

    def division(self, number_1, number_2):
        """ a simple function performs multiplication and division,
        in case of division by 0 a warning"""
        self.last_result = self.result
        if number_2 == 0:
            return 'division by 0 is not allowed'
        else:
            self.result = number_1 * number_2
        return self.result


set_1 = MathOper()

print(set_1.last_result)
set_1.add(1, 1)
print(set_1.last_result)
set_1.multi(2, 3)
print(set_1.last_result)
set_1.multi(3, 4)
print(set_1.last_result)
set_1.multi(3, 4)
print(set_1.last_result)
