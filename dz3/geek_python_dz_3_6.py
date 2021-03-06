# Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же, но с прописной
# первой буквой. Например, print(int_func(‘text’)) -> Text.

def int_func(string):
    """
    Функция переводит в верхний регистр первый символ всех слов в строке
    :param string: Входящая строка
    :return: Результат - строка из слов с первой буквой в верхем регистре
    """
    # Возвращаем строку состоящую из 0-го символа, обработанного методом upper()
    # с конкатенацией среза строки с 1-го символа
    # return str(string)[0].upper() + str(string)[1:] - первоначальный вариант с одним словом

    # делим строку пробелами
    str_list = str(string).split(sep=' ')
    # инициализируем пустую строку для результата преобразования
    new_str = ""
    # обрабатываем слова
    for i in str_list:
        # конкатенация результата с 0-м символом каждого слова, обработанного методом upper()
        # и среза строки (слова) с 1-го символа, плюс пробел
        new_str = new_str + i[0].upper() + i[1:] + " "
    # возвращаем результат
    return new_str

# Запрос строки
str_test = input("Введите строку из слов в нижнем регистре >>> ")
print (int_func(str_test))
