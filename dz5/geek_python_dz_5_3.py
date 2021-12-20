# Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк).
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.
# файл employees.txt в комплекте

count = 0
total = 0

try:
    # открываем файл
    with open('employees.txt','r',encoding='UTF-8') as employees_file:
        for line in employees_file:
            # отмечаем плюсами сотрудников с ЗП > 20 000
            if int(line.split()[1]) > 20000:
                print(f' +++++++ {line}',end='')
            # остальных просто выводим, для наглядности
            else:
                print(line,end='')
            # увеличиваем счётчик, суммируем ЗП, для простоты в int
            count +=1
            total += int(line.split()[1])
except:
    print('Ошибка при открытии файла employees.txt')
# выводим итоги
print(f'\n=========================\nИтого сотрудников - {count}\nСредняя ЗП - {total/count}')