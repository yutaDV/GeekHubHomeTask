'''НT4.  Створіть функцію <morse_code>, яка приймає на вхід рядок
у вигляді коду Морзе та виводить декодоване значення (латинськими літерами).
Особливості:
 - використовуються лише крапки, тире і пробіли (.- )
 - один пробіл означає нову літеру
 - три пробіли означають нове слово
 - результат може бути case-insensitive (на ваш розсуд
   великими чи маленькими літерами).
 - для простоти реалізації - цифри, знаки пунктуацїї, дужки, лапки тощо
    використовуватися не будуть. Лише латинські літери.
 - додайте можливість декодування сервісного сигналу SOS (...---...)
    Приклад:
    --. . . -.- .... ..- -...   .. ...   .... . .-. .
результат: GEEKHUB IS HERE'''


def morse_code(message: str):
    '''Morse language translation function'''

    DEF_DICT = {
        'A': '.-', 'B': '-...', 'C': '-.-.',
        'D': '-..', 'E': '.', 'F': '..-.',
        'G': '--.', 'H': '....', 'I': '..',
        'J': '.---', 'K': '-.-',
        'L': '.-..', 'M': '--', 'N': '-.',
        'O': '---', 'P': '.--.', 'Q': '--.-',
        'R': '.-.', 'S': '...', 'T': '-',
        'U': '..-', 'V': '...-', 'W': '.--',
        'X': '-..-', 'Y': '-.--', 'Z': '--..',
        'SOS': '...---...'
    }
    for letter in message:
        if letter not in '.- ':
            return'Not correct message'
    words = message.split('   ')
    word_and_letter = []
    for word in words:
        letter = word.split(' ')
        word_and_letter.append(letter)
    result = ''
    for word in word_and_letter:
        for letter in word:
            for key, value in DEF_DICT.items():
                if value == letter:
                    result += key
        result += " "
    return result


print(morse_code(input('Enter the morse code:')))
