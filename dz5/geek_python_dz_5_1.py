# Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

# контекст управления
try:
    with open('str_input_file.txt','w') as str_input_file:
        # вводим строки, пишем их в файл, до тех пор, пока не будет введена пустая строка
        while True:
            input_string = input('Введите стоки файла (Пустая строка - окончание ввода) >>>')
            # если строка не пустая
            if input_string:
                # пишем в файл
                print(input_string,file=str_input_file)
            # если пустая
            else:
                # выходим из цикал
                break
# обрабатываем возможное исключение при открытии файла
except:
    print('Ошибка при открытии файла str_input_file.txt')