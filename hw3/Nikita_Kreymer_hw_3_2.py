def num_translate_adv():
    number = input('Введите число на английском: ')
    if number.istitle():
        print(numbers.get(number.lower()).title())
    else:
        print(numbers.get(number.lower()))


numbers = {
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре',
    'five': 'пять',
    'six': 'шесть',
    'seven': 'семь',
    'eight': 'восемь',
    'nine': 'девять',
    'ten': 'десять',
}

num_translate_adv()
