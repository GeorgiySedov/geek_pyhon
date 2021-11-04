seconds_input = int(input ("Введите время в секундах >>> "))

#Считаем часы, если секунд >=3600
if seconds_input >= 3600:
    hours = seconds_input//3600
else:
    hours = 0
# Считаем минуты, если секунд > 60, (от остатка деления на 3600)
if seconds_input > 60:
    minutes = (seconds_input % 3600)//60
else:
    minutes = 0

# Считаем секунды, если их больше 0, (от остатка деления на 60)
if seconds_input > 0:
    seconds = (seconds_input % 60)
else:
    seconds = 0

print ("\n",hours,":",minutes,":",seconds)