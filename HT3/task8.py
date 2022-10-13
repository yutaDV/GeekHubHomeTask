'''TASK #8 Створити цикл від 0 до ... (вводиться користувачем).
 В циклі створити умову, яка буде виводити поточне значення,
 якщо остача від ділення на 17 дорівнює 0'''

while True:
    try:
        number = int(input("Please, enter a number greater than zero:  "))
        break
    except ValueError:
        print("Oops!!! That was no valid number. Try again...")

if number < 0:
    print('Sorry, I do not have any results for you')
else:
    print('Your results:')
    for i in range(number):
        if i % 17 == 0:
            print(i)
