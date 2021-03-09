"""
7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте перегрузку
методов сложения и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры класса (комплексные числа)
и выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.
"""


class ComplexNumber:
    real_part: float
    img_part: float
    
    def __init__(self, real_part: float, img_part: float = 0):
        self.complex_number = complex(real_part, img_part)

    def __add__(self, other):
        if isinstance(other, ComplexNumber):
            return f"Результат сложения: {self.complex_number + other.complex_number}"
        else:
            return "Складываемые числа не являются комплексными"

    def __mul__(self, other):
        if isinstance(other, ComplexNumber):
            return f"Результат умножения: {self.complex_number * other.complex_number}"
        else:
            return "Умножаемые числа не являются комплексными"


if __name__ == "__main__":
    complex_number_1 = ComplexNumber(1, 2)
    complex_number_2 = ComplexNumber(2, -4)
    print(complex_number_1 + complex_number_2)
    print(complex_number_1 * complex_number_2)
