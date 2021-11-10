seconds_input = int(input ("Введите время в секундах >>> "))

#Считаем часы
hours = seconds_input//3600

# Считаем минуты
minutes = (seconds_input % 3600)//60

# Считаем секунды
seconds = (seconds_input % 60)

#print ("\n",hours,":",minutes,":",seconds)
print (f'\n{hours} : {minutes} : {seconds}')