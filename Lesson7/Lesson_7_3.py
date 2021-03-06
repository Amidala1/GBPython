"""
3. Реализовать программу работы с органическими клетками, состоящими из ячеек. Необходимо создать класс Клетка.
В его конструкторе инициализировать параметр, соответствующий количеству ячеек клетки (целое число).
В классе должны быть реализованы методы перегрузки арифметических операторов: сложение (add()), вычитание (sub()),
умножение (mul()), деление (truediv()). Данные методы должны применяться только к клеткам и выполнять увеличение,
уменьшение, умножение и целочисленное (с округлением до целого) деление клеток, соответственно.
Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность количества ячеек двух клеток
больше нуля, иначе выводить соответствующее сообщение.
Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется как произведение количества ячеек
этих двух клеток.
Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется как целочисленное деление количества
ячеек этих двух клеток.
В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду.
Данный метод позволяет организовать ячейки по рядам.
Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу.
Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5. Тогда метод make_order() вернет строку:
*****\n*****\n**.
Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5. Тогда метод make_order() вернет строку:
*****\n*****\n*****.
"""

from sys import exit


class Cell:
    cells_number: int

    def __init__(self, cells_number: int):
        self.cells_number = cells_number

    def __add__(self, other: "Cell"):
        return f"Число ячеек общей клетки (результат сложения): {self.cells_number + other.cells_number}"

    def __sub__(self, other: "Cell"):
        return f"Разность количества ячеек двух клеток: {self.cells_number - other.cells_number}" \
            if (self.cells_number - other.cells_number) > 0 \
            else f"Разность количества ячеек двух клеток меньше нуля"

    def __mul__(self, other: "Cell"):
        return f"Число ячеек общей клетки (результат умножения): {self.cells_number * other.cells_number}"

    def __truediv__(self, other: "Cell"):
        try:
            return f"Число образовавшихся клеток: {self.cells_number // other.cells_number}"
        except ZeroDivisionError:
            return "Деление на ноль"

    def make_order(self, per_raw):
        ordered_cell = ""
        raw = "*" * self.cells_number
        for x in range(0, self.cells_number, per_raw):
            ordered_cell += raw[x:x + per_raw] + "\n"

        return ordered_cell


# функция для валидации введенного пользователем значения
def validate_user_input(hello_text):
    while True:
        try:
            value = int(input(hello_text))
        except ValueError:
            print("Пожалуйста, введите корректное значение")
        else:
            return value


if __name__ == "__main__":
    try:
        cells_number_1 = validate_user_input("Введите кол-во ячеек первой клетки: ")
        cells_number_2 = validate_user_input("Введите кол-во ячеек второй клетки: ")
        cell_1 = Cell(cells_number_1)
        cell_2 = Cell(cells_number_2)
        print("{}\n{}\n{}\n{}\n".format(cell_1 + cell_2, cell_1 - cell_2, cell_1 * cell_2, cell_1 / cell_2))
        per_raw = validate_user_input("Введите желаемое кол-во ячеек в ряду: ")
        print("Произведена организация ячеек клеток по рядам: \n{}\n___\n{}".format(cell_1.make_order(per_raw),
                                                                                    cell_2.make_order(per_raw)))
    except KeyboardInterrupt:
        print("\nВы вышли из программы")
        exit(0)
