def get_count_char(str_):

    DEFAULT_COUNT = 0
    dict_of_num_and_char = {}  # создание словаря букв и их количества

    str_ = str_.lower()  # перевод букв из верхнего регистра в нижний со всего текста

    for char in str_:  # перебор всех символов в тексте
        if char.isalpha():  # проверка является ли символ буквой и запись в словарь буквы и ее количества
            dict_of_num_and_char[char] = dict_of_num_and_char.get(char, DEFAULT_COUNT) + 1

    return dict_of_num_and_char

def percent_of_chars(dict_):

    number_of_chars = sum(dict_.values())  # количество всех символов в тексте

    for char in dict_:  # запись нового словаря через формулу процентного соотношения количества конкретной буквы ко всем буквам
        dict_[char] = round(dict_.get(char)/number_of_chars * 100, 2)

    return dict_  # результат каждой буквы приведен к % и округлен до 2х знаков после запятой


main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))
print(percent_of_chars(get_count_char(main_str)))
