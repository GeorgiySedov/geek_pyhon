# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. При этом английские
# числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.
# файл ciphers_file.txt в комплекте

# открываем файлы
read_file = open('ciphers_file.txt','r',encoding='utf-8-sig')
write_file = open('ciphers_convert.txt','w',encoding='utf-8-sig')

# читаем построчно, заменяем числительные на русские
for line in read_file:
    if line.count('One') > 0:
        newline = line.replace("One","Один")
    elif line.count('Two') > 0:
        newline = line.replace('Two','Два')
    elif line.count('Three') > 0:
        newline = line.replace('Three', 'Три')
    elif line.count('Four') > 0:
        newline = line.replace('Four','Четыре')
    else:
        newline = line
    # пишем в другой файл (ciphers_convert.txt), выводим на экран
    print(newline,file=write_file,end='')
    print(newline, end='')
# закрываем файлы
read_file.close()
write_file.close()