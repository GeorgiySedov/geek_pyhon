# Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина). Значения данных
# атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными. Определить метод расчета
# массы асфальта, необходимого для покрытия всего дорожного полотна. Использовать формулу: длина*ширина*масса асфальта
# для покрытия одного кв метра дороги асфальтом, толщиной в 1 см*число см толщины полотна. Проверить работу метода.
# Например: 20м*5000м*25кг*5см = 12500 т

class Road ():
    _lenght: int
    _width: int
    cost: int
    thikness: int

    def __init__(self, length, width, cost = 25, thickness = 5):
        self._lenght = length
        self._width = width
        self.cost = cost
        self.thikness = thickness

    def calculate (self):
        total = self._lenght * self._width * self.cost * self.thikness
        print(f'Расход асфальта при параметрах: \nДлина:{self._lenght} м'
              f'\nШирина: {self._width} м'
              f'\nТолщина слоя: {self.thikness} см'
              f'\nРасход на м2 при толщине 1см: {self.cost} кг'
              f'\n=========================',end='')
        if total >= 1000:
            total = round(total / 1000, 3)
            print(f'\nСоставит: {total} тонн')
        else:
            print(f'\nСоставит: {total} кг')

road1 = Road(1,1)
road1.calculate()