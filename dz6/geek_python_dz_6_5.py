# Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и метод
# draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш),
# Handle (маркер). В каждом из классов реализовать переопределение метода draw. Для каждого из классов метод должен выводить
# уникальное сообщение. Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
# базовый класс с конструктором
class Stationery():
    title: str
    def __init__(self,name):
        self.title = name
    def draw(self):
        print(f'{self.title} - Базовая отрисовка')
# Дочерние классы с переопределением метода Draw
class Pen(Stationery):
    def draw(self):
        print(f'{self.title} - Рисовка ручкой')
class Pencil(Stationery):
    def draw(self):
        print(f'{self.title} - Прорисовка карандашом')
class Handle(Stationery):
    def draw(self):
        print(f'{self.title} - Зарисовка маркером')

stat1=Stationery('Принадлежность')
stat1.draw()
pen1=Pen('Ручка1')
pen1.draw()
pencil1=Pencil('Карандаш1')
pencil1.draw()
handle1=Handle('Маркер1')
handle1.draw()
