# Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод init()), который должен принимать данные
# (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц: см. в методичке.
#
# Следующий шаг — реализовать перегрузку метода str() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода add() для реализации операции сложения двух объектов класса Matrix (двух матриц).
# Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем с
# первым элементом первой строки второй матрицы и т.д.

class Matrix():
    matrix = []
    def __init__(self, list: list):
        self.matrix = list

    def __add__(self, other):
        if isinstance(other,Matrix):
            height = len(self.matrix)
            width = len(self.matrix[0])
            sum_matrix = []
            for i in range(height):
                sum_matrix.append([])
                for j in range(width):
                    sum_matrix[i].append(self.matrix[i][j] + other.matrix[i][j])
            return sum_matrix
        else:
            return None

    def __str__(self):
        print_string = ''
        height = len(self.matrix)
        width = len(self.matrix[0])
        for i in range(height):
            if i > 0: print_string +='\n'
            for j in range(width):
                print_string += str(self.matrix[i][j])
                if j < width: print_string += ' '
        return print_string

TestMatrix = Matrix([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
TestMatrix2 = Matrix([[21,22,23],[24,25,26],[27,28,29],[30,31,32]])

print(f'Первая матрица:\n{TestMatrix}\n')
print(f'Вторая матрица:\n{TestMatrix2}\n')

Matrix3 = Matrix(TestMatrix + TestMatrix2)
print(f'Сумма двух первых матриц:\n{Matrix3}')