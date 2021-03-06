"""
1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который должен
принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Следующий шаг — реализовать перегрузку метода str() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода add() для реализации операции сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем
с первым элементом первой строки второй матрицы и т.д.
"""
from random import randint
from sys import exit


class Matrix:
    rows_count: int
    columns_count: int

    def __init__(self, rows_count: int = 1, columns_count: int = 1):
        self.rows_count = rows_count
        self.columns_count = columns_count
        self.start_number = 0
        self.end_number = 1000
        self.matrix = []
        self.matrix_size = frozenset([self.rows_count, self.columns_count])

        # создание рандомной матрицы
        while self.rows_count != 0:
            self.matrix.append([randint(self.start_number, self.end_number) for x in range(self.columns_count)])
            self.rows_count -= 1

    def __str__(self):
        return str("\n".join(["\t".join([str(col) for col in raw]) for raw in self.matrix]))

    def __add__(self, other: "Matrix"):
        if self.matrix_size != other.matrix_size:
            print("Операция сложения невозможна для матриц с разными размерами.")
            exit(1)

        result_matrix = []
        for item in zip(self.matrix, other.matrix):
            temp = []
            for numbers in zip(item[0], item[1]):
                temp.append(sum(numbers))
            result_matrix.append(temp)

        return str("\n".join(["\t".join([str(col) for col in raw]) for raw in self.matrix]))


if __name__ == "__main__":
    exit_flag = False
    while not exit_flag:
        try:
            r_count_1, c_count_1, r_count_2, c_count_2 = int(input("Введите кол-во строк первой матрицы: ")), \
                                                         int(input("Введите кол-во столбцов первой матрицы: ")), \
                                                         int(input("Введите кол-во строк второй матрицы: ")), \
                                                         int(input("Введите кол-во столбцов второй матрицы: "))
        except ValueError:
            print("Введите числовые значения")
        except KeyboardInterrupt:
            print("\nВы вышли из программы")
            exit(0)
        else:
            if r_count_1 <= 0 or c_count_1 <= 0 or r_count_2 <= 0 or c_count_2 <= 0:
                print("Введите значение больше нуля")
            else:
                exit_flag = True
                matrix1 = Matrix(r_count_1, r_count_1)
                matrix2 = Matrix(r_count_2, r_count_2)
                print("Первая сгенерированная матрица:\n{}\n___"
                      "\nВторая сгенерированная матрица:\n{}\n___"
                      "\nРезультирующая матрица:\n{}".format(matrix1, matrix2, matrix1 + matrix2))