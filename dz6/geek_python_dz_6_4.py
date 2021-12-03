# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
# который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

class Car():
    speed: float
    color: str
    name: str
    is_police: bool
    def __init__(self,speed:float,color:str,name:str,is_police: bool):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
    def go(self):
        print(f'{self.color} {self.name} поехала')
    def stop(self):
        print(f'{self.color} {self.name} остановилась')
    def turn(self,direction):
        print(f'{self.color} {self.name} повернула {direction}')
    def show_speed(self):
        print(f'Текущая скорость {self.color} {self.name} = {self.speed}')

class TownCar(Car):
    def show_speed(self):
        print(f'Текущая скорость {self.color} {self.name} = {self.speed}')
        if self.speed > 60:
            print(f'Скорость {self.color} {self.name} превышена !')

class WorkerCar(Car):
    def show_speed(self):
        print(f'Текущая скорость {self.color} {self.name} = {self.speed}')
        if self.speed > 40:
            print(f'Скорость {self.color} {self.name} превышена !')

class SportCar(Car):
    def show_speed(self):
        print(f'Текущая скорость {self.color} {self.name} = {self.speed}')

class PoliceCar(Car):
    def show_speed(self):
        print(f'Текущая скорость {self.color} {self.name} = {self.speed}')

car1 = Car(120,'зелёный','Москвич',0)
car2 = TownCar(90,'красный','Жигули',0)
car3 = WorkerCar(50,'синий','Камаз',0)
car4 = PoliceCar(75,'чёрный','Форд фокус',1)
car5 = SportCar(155,',белый','Порш',0)

car1.go()
car1.show_speed()
print(f'имя - {car1.name}')
car1.turn('налево')
car1.stop()
print('================')
car2.go()
print (f'цвет - {car2.color}')
car2.turn('направо')
print (f'{car2.color} {car2.name} is_police = {car2.is_police}')
car2.show_speed()
print('================')
car3.go()
print (f'скорость - {car3.speed}')
car3.show_speed()
car3.stop()