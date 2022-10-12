'''TASK #8 Створити цикл від 0 до ... (вводиться користувачем).
 В циклі створити умову, яка буде виводити поточне значення,
 якщо остача від ділення на 17 дорівнює 0'''

number = int(input("Please, input a number:  "))

if number < 17:
    print('Sorry, I do not have any result for you')
else:
    print('your results:')
    for i in range(number):
        if i > 0 and i % 17 == 0:
            print(i)
