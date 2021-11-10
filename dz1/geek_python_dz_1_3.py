# запрашиваем ввод числа
a = int(input ('Введите число >>> '))

# суммируем, преобразуя типы
b = a + int(str(a)+str(a)) + int(str(a)+str(a)+str(a))

# выводим результат
print ('Сумма ',a, ' + ',str(a)+str(a),' + ',str(a)+str(a)+str(a),' = ',b)