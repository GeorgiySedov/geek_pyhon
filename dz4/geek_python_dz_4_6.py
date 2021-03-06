# Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
#
# Подсказка: использовать функцию count() и cycle() модуля itertools. Обратите внимание, что создаваемый цикл не должен
# быть бесконечным. Необходимо предусмотреть условие его завершения.
#
# Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл. Во втором также
# необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.

from itertools import count
from itertools  import cycle
from random import randint

# итератор для count от 3
cipher_list_count  = (x for x in count(3))

# итератор для cycle из 5 случайных значений (1-15)
cipher_list_cycle = cycle((randint(1,15) for i in range(5)))

# вывод значений из бесконечного итератора, (ограничение до 10)
el = 0
while el < 10:
    el = next(cipher_list_count)
    print(el)

# вывод значений из циклического итератора (20 элементов, т.е 4 цикла по 5 значений)
i = 0
for el in cipher_list_cycle:
    print(el)
    if i > 20:
        break
    i += 1