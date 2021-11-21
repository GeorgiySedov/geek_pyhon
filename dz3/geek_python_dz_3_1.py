 # Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
 # Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

# Функция деления
def division (divided,divisor):
 """
 Функция осуществляющая деление чисел
 :param divided: Делимое
 :param divisor: Делитель
 :return: Результат деления делимого на делитель
 """
 # Пробуем поделить делимое на делитель, округляем до 3-го знака для красоты
 try:
  result = round(divided / divisor,3)
 # Обрабатываем исключение "Деление на ноль" - ZeroDivisionError
 except ZeroDivisionError:
  result = 0
 return result

divided = int(input("Введите делимое >>> "))
divisor = int(input("Введите делитель >>> "))

print (f"{divided} / {divisor} = {division(divided,divisor)}")