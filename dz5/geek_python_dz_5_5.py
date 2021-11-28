# Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами. Программа
# должна подсчитывать сумму чисел в файле и выводить ее на экран.

from random import randint

# генерируем список из 40 случайных чисел 1-35
cipher_list = [randint(1,35) for x in range(20)]

# пишем список в файл rand_cipher.txt через пробел
with open('rand_cipher.txt','w',encoding='utf-8-sig') as cipher_file:
    for el in cipher_list:
        cipher_file.write((str(el)+' '))

# счётчик в ноль
total = 0

# открываем файл на чтение, читаем строку, делим в список, разделитель - пробел
with open('rand_cipher.txt','r',encoding='utf-8-sig') as cipher_file:
    cipher_list = cipher_file.readline().split(sep=' ')
    # проходим по списку, конвертируем в int, суммируем через try, чтобы обработать исключения типов
    print(cipher_list)
    for el in cipher_list:
        try:
            total += int(el)
        except:
            continue

print(f'Сумма чисел {total}')