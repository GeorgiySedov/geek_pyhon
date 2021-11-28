# Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
# практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого предмета не
# обязательно были все типы занятий. Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
# Вывести словарь на экран.
# (файл disciplines.txt в комплекте)
# импортируем модуль с регулярными выражениями
import re

# печатаем содержимое файла для наглядности
with open('disciplines.txt','r',encoding='utf-8-sig') as discipline_file:
    print(f'\n{discipline_file.read()}')

# инициализируем пустой словарь
discipline_dict={}
with open('disciplines.txt','r',encoding='utf-8-sig') as discipline_file:
    for line in discipline_file:
        # отделяем 0-й элемент списка (сконвертированного из строки методом split), убираем суффикс ':'
        discipline_key = line.split(' ')[0].removesuffix(':')
        # обнуляем счётчик часов
        discipline_value = 0
        # считаем часы, выбирая их методом findall регулярным выражением \d+ (одна или более цифр)
        for el in re.findall('\d+',line):
            discipline_value += int(el)
        # добавляем пару ключ:значение в словарь
        discipline_dict[discipline_key] = discipline_value

# печатаем словарь
print(f'\n{discipline_dict}')