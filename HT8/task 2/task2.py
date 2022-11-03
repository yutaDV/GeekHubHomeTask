'''НT8.2.   Написати функцію, яка приймає два параметри: ім'я (шлях) файлу
та кількість символів. Файл також додайте в репозиторій. На екран має бути
виведений список із трьома блоками - символи з початку, із середини та з кінця
файлу. Кількість символів в блоках - та, яка введена в другому параметрі.
Придумайте самі, як обробляти помилку, наприклад, коли кількість символів
більша, ніж є в файлі або, наприклад, файл із двох символів і треба вивести
по одному символу, то що виводити на місці середнього блоку символів?).
Не забудьте додати перевірку чи файл існує. '''


def open_file(name, amount):
    '''The function takes a file and returns 3 parts of it'''

    try:
        f = open(name)
    except FileNotFoundError:
        return 'Dont found the file'
    else:
        f.close()
    if not isinstance(amount, int):
        return 'This is invalid value. The second argument must be a number'
    if amount < 1:
        return 'The second argument must be greater than 0'
    with open(name) as file:
        result = []
        len_fale = len(file.read())
        if len_fale == 0:
            return 'The file is emty'
        if len_fale < amount:
            return f'Invalid arguments, amount cannot be begger than{len_fale}'
        file.seek(0)
        result.append(file.read(amount))
        file.seek(len_fale // 2 - amount // 2)
        result.append(file.read(amount))
        file.seek(len_fale - amount)
        result.append(file.read(amount))
        return result


if __name__ == "__main__":
    print(open_file('doc_ht8_2.txt', -156))
