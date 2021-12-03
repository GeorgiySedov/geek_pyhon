# Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность), income
# (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия, например,
# {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker. В классе Position реализовать
# методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income). Проверить работу
# примера на реальных данных (создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать
# методы экземпляров).

# класс Worker
class Worker():
    name: str
    surname: str
    position: str
    _income = dict()
    # конструктор класса
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income['wage'] = wage
        self._income['bonus'] = bonus

# класс Position наследуем от Worker
class Position(Worker):
    # возвращаем полное имя
    def get_full_name(self):
        return self.name + ' ' + self.surname
    # возвращаем доход с учётом премии
    def get_total_income(self):
        return self._income["wage"]+self._income["bonus"]

# создаём экземпляр класса, с первоначальными данными
john = Position("John", "Doe", "manager", 150, 100)

# Выводим полное имя и общий доход с учётом премии
print (f'{john.get_full_name()}\'s total income = ${john.get_total_income()}')