# Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится месяц
# (зима, весна, лето, осень). Напишите решения через list и через dict.

# список времён года, для деления нацело на 3, две зимы, чтоб захватить декабрь
seasons_list = ["зима","весна","лето","осень","зима"]
seasons_dict = {0:'зима',1:'весна',2:'лето',3:'осень',4:'зима'}

# вводим номер месяца
inp_season = int(input("Введите номер месяца 1-12 >>> "))

# делим нацело на 3, подставляем элемент по индексу (ключу), зима будет 0,1,12
print (f"{inp_season}-й месяц принадлежит ко времени года {seasons_list[inp_season//3]} (список)" )
print (f"{inp_season}-й месяц принадлежит ко времени года {seasons_dict.get(inp_season//3)} (словарь)")