# Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка должна содержать данные о фирме:
# название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
#
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма получила
# убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
#
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

import json
# инициализация счётчиков, словарей
avg_profit = 0
profit_count = 0
json_list = []
firms_dict={}
avg_profit_dict = {}

# открываем файл, читаем, разбираем методом split
with open('firms.txt','r',encoding='utf-8-sig') as firms_file:
    for line in firms_file:
        print(line,end='')
        firms_list = line.split(' ')
        # вычисляем прибыль
        firm_profit = int(firms_list[2]) - int(firms_list[3])
        # заполняем словарь
        firms_dict[firms_list[0]] = firm_profit
        # если прибыль больше нуля, добавляем её к сумме для вычисления средней
        if firm_profit > 0:
            avg_profit += firm_profit
            profit_count += 1
# заполняем словарь со средней прибылью
avg_profit_dict['average_profit'] = round(avg_profit / profit_count)
# заполняем словарь для json
json_list.append(firms_dict)
json_list.append(avg_profit_dict)

# выводим на экран, для наглядности
print(json_list)

# записываем json в файл
with open('firms_json.txt','w',encoding='utf-8-sig') as firms_json_file:
    json.dump(json_list,firms_json_file,ensure_ascii=False, )