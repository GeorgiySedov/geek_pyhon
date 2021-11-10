# запрашиваем ввод выручки и издержек
revenue = int (input('Введите значение выручки >>> '))
cost = int (input('Введите значение издержек >>> '))

# если прибыль
if revenue > cost:
    print ('Фирма работает с прибылью\n')
    # считаем доход
    profit = revenue - cost
    # доходность
    profitability = profit / revenue
    # на сотрудника
    emploee = int (input('Введите численность персонала >>> '))
    profit_empl = profit / emploee
    # выводим результтаты
    print ('Прибыль фирмы - ', profit)
    print ('Прибыльность фирмы - ', profitability)
    print ('Прибыль в рассчёте на одного сотрудника - ', profit_empl)
    #если в убыток
elif cost > revenue:
    print ('Фирма работает в убыток\n')
    # если в ноль
else:
    print ('Фирма работает в ноль\n')