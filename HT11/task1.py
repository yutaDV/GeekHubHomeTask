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

''' ВЕЛИКА ЙМОВІРНІСТЬ ЩО Я ЗОВСІМ НЕ ЗРОЗУМІЛА ДАНЕ ЗАВДАННЯ, ПРОТЕ
НЕ ГОДИТЬСЯ ПРОСИТИ ДОПОМОГИ НЕ СПРОБУВАВШИ ЗРОБИТИ САМОСТІЙНО '''


class MathOperations:
    last_result = None

    """The class performs arithmetic operations with two numbers +, -, /, *

    The class includes four objects, two of which have int or float
    which are the arguments of mathematical operations, the other two
    are the default - None that store the current and previous result """

    def __init__(self, number_1, number_2, last_result=None, result=None):
        """the constructor of a class describes the attributes of the class"""
        if isinstance(number_1, float) or isinstance(number_1, int):
            self.number_1 = number_1
        else:
            raise TypeError('number must be of type float or int')

        if isinstance(number_2, float) or isinstance(number_2, int):
            self.number_2 = number_2
        else:
            raise TypeError('number must be of type float or int')
        self.result = None
        self.last_result = self.result
        """saving the previous result"""

    def add(self):
        """ a simple function adds two numbers"""
        self.result = self.number_1 + self.number_2
        return self.result

    def subtraction(self):
        """ a simple function subtracts the second number from the first"""
        self.result = self.number_1 - self.number_2
        return self.result

    def multiplication(self):
        """a simple function multiplies two numbers"""
        self.result = self.number_1 * self.number_2
        return self.result

    def division(self):
        """ a simple function performs multiplication and division,
        in case of division by 0 a warning"""
        if self.number_2 == 0:
            return 'division by 0 is not allowed'
        else:
            self.result = self.number_1 * self.number_2
        return self.result


numbers1 = MathOperations(1, 2)
numbers2 = MathOperations(1, 0)
numbers3 = MathOperations(1, 5)
