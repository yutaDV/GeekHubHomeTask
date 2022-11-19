'''НT12. 3   Створіть клас в якому буде атрибут який буде рахувати кількість
 створених екземплярів класів.'''


class Customers:
    count = 0

    def __init__(self):
        Customers.count += 1


p1 = Customers()
print(p1.count)
p2 = Customers()
print(p2.count)
p3 = Customers()
print(p3.count)
