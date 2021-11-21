# Программа запрашивает у пользователя строку чисел, разделенных пробелом. При нажатии Enter должна выводиться сумма чисел.
# Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter. Сумма вновь введенных чисел будет
# добавляться к уже подсчитанной сумме. Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной ранее
# сумме и после этого завершить программу.

summa = 0

def inc_sum(string):
    """
    Функция получает на входе строку,состоящую из чисел разделённых пробелами
    Суммирует числа, выводит сумму
    Если в строке не число - выводит сумму, завершает выполнение
    :param string: Входящая строка (числа, разделённые пробелами)
    """
    # глобальная переменная для суммы
    global summa
    # делим строку на составные части, разделитель - прообле
    str_list = str(string).split(sep=' ')
    # пробуем суммировать к глобальной переменной, проверяя на конвертацию в целые числа
    for i in str_list:
        try:
            summa = summa + int(i)
        # если не целое число, выводим сумму и выходим
        except:
            print(f"Сумма чисел {summa}")
            exit(0)
    print(f"Сумма чисел {summa}")

# Цикл, запрашивающий строки чисел, (обработка и вывод в функции)
while (True):
    # приглашение с разъяснением правил
    print("Введите строку чисел, разделённых пробелами")
    print("Для выхода введите спец.символ")
    # ввод строки для функции
    str1 = (input(">>> "))
    inc_sum(str1)