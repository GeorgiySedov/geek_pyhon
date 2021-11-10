seconds_input = int(input ("Введите время в секундах >>> "))

#Считаем часы
hours = seconds_input//3600

# Считаем минуты
minutes = (seconds_input % 3600)//60

# Считаем секунды
seconds = (seconds_input % 60)

# выводим результат
print (f'\n{hours:2d} : {minutes:2d} : {seconds:2d}')