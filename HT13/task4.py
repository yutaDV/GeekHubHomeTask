'''HT 13  4. Створіть клас, який буде повністю копіювати поведінку
list, за виключенням того, що індекси в ньому мають починатися з 1,
а індекс 0 має викидати помилку (такого ж типу, яку кидає list якщо
звернутися до неіснуючого індексу)'''


class BrokenList(list):

    def __getitem__(self, index):
        if index == 0:
            raise 'IndexErro'
        if index < 0:
            index = index
        else:
            index = index - 1
        return list.__getitem__(self, index)


mylist = [7, 2, 3, 5, 6]
my_list = BrokenList([7, 2, 3, 5, 6])
my_list_1 = BrokenList('kdsjhgdfhgkhkdghkgdhgd')
print(my_list[1])
print(mylist[1])
print(my_list[-1])
print(mylist[-1])
print(my_list[5])
print(my_list_1[1])
print(my_list_1[22])
print(my_list[0])
