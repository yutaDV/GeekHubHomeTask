''' HT 13.3 Реалізуйте класс Transaction. Його конструктор повинен
приймати такі параметри:
- amount - суму на яку було здійснено транзакцію
- date - дату переказу
- currency - валюту в якій було зроблено переказ (за замовчуванням USD)
- usd_conversion_rate - курс цієї валюти до долара (за замовчуванням 1.0)
- description - опис транзакції (за дефолтом None)
Усі параметри повинні бути записані в захищені (_attr) однойменні атрибути.
Доступ до них повинен бути забезпечений лише на читання та за допомогою
механізму property. При чому якщо description дорівнює None,
то відповідне property має повертати рядок "No description provided".
Додатково реалізуйте властивість usd, що має повертати суму переказу
у доларах (сума * курс)'''


class Transaction:

    def __init__(self, amount, date, currency='USD', usd_conversion_rate=1.0, description=None):    
        self._amount = amount
        self._date = date
        self._currency = currency
        self._usd_conversion_rate = usd_conversion_rate
        self._description = description

    @property
    def amount(self):
        return self._amount

    @property
    def date(self):
        return self._date

    @property
    def currency(self):
        return self._currency

    @property
    def usd_conversion_rate(self):
        return self._usd_conversion_rate

    @property
    def description(self):
        if self._description is None:
            return "No description provided"
        else:
            return self._description

    @property
    def usd(self):
        currency_dict = {
            'USD': 1,
            'EUR': 1.04,
            'UAH': 0.028,
            'GBP': 1.21
        }
        for key, value in currency_dict.items():
            if key == self._currency:
                return self._amount * value
        return 'unknown currency'


trans_1 = Transaction(1500, '24.11.1995', 'UAH', 0.028, 'exchange')
trans_2 = Transaction(800, '24.11.2016')
trans_3 = Transaction(50, '24.11.1995', 'EUR', 1.02)


print(trans_1._usd_conversion_rate)
print(trans_1.usd_conversion_rate)
print(trans_3.description)
print(trans_3._description)
print(trans_2.currency)
print(trans_2._currency)
print(trans_1.usd)
print(trans_2.usd)
print(trans_3.usd)
