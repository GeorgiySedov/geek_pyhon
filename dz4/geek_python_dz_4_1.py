# Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах*ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

# Тестовые параметры заданы в св-вых запуска файла (10, 8.5, 50)

from sys import argv

def pay_calculation (hours_count, tax_per_hour, bonus):
    """
    функция расчёта ЗП
    :param hours_count: кол-во часов
    :param tax_per_hour: ставка в час
    :param bonus: премия
    :return: итоговая ЗП
    """
    return tax_per_hour * hours_count + bonus


try:
     hours_count = float(argv[1])
     tax_per_hour = float(argv[2])
     bonus = float(argv[3])
except ValueError:
     print("\nОшибка: неверный тип параметра")
     print("Использование:\nимя_программы кол-во_часов ставка_в_час премия")
     exit(1)
except IndexError:
    print("\nОшибка: слишком мало параметров")
    print("Использование:\nимя_программы кол-во_часов ставка_в_час премия")
    exit(1)

print (f"\nЧасов отработано: {hours_count}\nСтавка в час: {tax_per_hour}\nПремия: {bonus}\n\n"
       f"=================================\n"
       f"Итого к выплате: {pay_calculation(hours_count, tax_per_hour, bonus)}")