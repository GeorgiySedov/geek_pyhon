# Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.
# файл count_string_words.txt в комплекте

# пробуем открыть файл
try:
    with open('count_string_words.txt','r') as count_file:
        # читаем строки
        file_strings = count_file.readlines()
except:
# общее исключения для обработки ошибок
    print('Ошибка при открытии файла count_string_words.txt')

print('\nСодержимое файла:\n')
# выводим содержимое файла
for str in file_strings:
    print(str,end='')

# выводим кол-во строк
print(f'\n\nВ файле - {len(file_strings)} строк\n')

# счётчик для нумерации вывода строк
i = 1
# считаем кол-во слов в строках, при помощи len и split

for str in file_strings:
    print(f'В {i}-й строке {len(str.split())} слов')
    i += 1