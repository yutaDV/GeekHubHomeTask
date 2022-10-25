'''НT7.6.   Напишіть функцію,яка приймає рядок з декількох слів
і повертає довжину найкоротшого слова. Реалізуйте обчислення за
допомогою генератора в один рядок.'''


def count_string(string):

    words = [len(word) for word in string.split(' ')]
    return(min(words))


print(count_string('kjhsajkhgd agjhjfd afjhdg'))
