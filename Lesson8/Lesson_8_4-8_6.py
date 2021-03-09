"""
4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
уникальные для каждого типа оргтехники.
5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу
в определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники,
а также других данных, можно использовать любую подходящую структуру, например словарь.
6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей,
изученных на уроках по ООП.
"""
from abc import ABC, abstractmethod
from sys import exit


class MyExceptions(Exception):
    """Исключения проекта"""

    def __init__(self, text):
        self.text = text

    def __str__(self):
        return f"Ошибка: {self.text}"


class UsefullMethodsClass:
    """Класс для хранения статических методов"""

    @staticmethod
    def validate_digit_data(hello_text: str):
        while True:
            try:
                number = input(hello_text)
                if number.isdigit() and int(number) != 0:
                    return int(number)
                else:
                    raise MyExceptions(f"Введите числовое значение, большее нуля!")
            except MyExceptions as e:
                print(e)

    @staticmethod
    def validate_str_data(hello_text: str):
        while True:
            try:
                value = input(hello_text)
                if value:
                    return value
                else:
                    raise MyExceptions("Пожалуйста, введите непустое значение")
            except MyExceptions as e:
                print(e)


class Stock:
    """Склад"""
    equipments: dict
    id_in_stock: int

    def __init__(self):
        self.equipments = {}
        self.id_in_stock = 0

    def store(self, equipment_object: "OfficeEquipment"):
        if isinstance(equipment_object, OfficeEquipment):
            self.equipments[self.id_in_stock] = equipment_object
            self.id_in_stock += 1
        else:
            raise MyExceptions(f"Добавляемый элемент {equipment_object} не является оргтехникой.")

        return self.equipments

    def filter_items(self, **kwargs):
        filtered_items_ids = []
        for key, value in self.equipments.items():
            if all([value.__getattribute__(key) == kwargs[key] for key in kwargs if (kwargs[key] is not None
                                                                                    and kwargs[key] != "")]):
                filtered_items_ids.append(key)

        return filtered_items_ids

    def transfer(self, depart_name: str, count: int, **kwargs):
        filtered_items_ids = self.filter_items(**kwargs)

        if len(filtered_items_ids) == 0:
            return "Не найдено оборудование, подходящее под введенные условия"
        elif count > len(filtered_items_ids):
            print(
                f"В наличии всего {len(filtered_items_ids)} оборудования из {count}. "
                f"Будет передано {count - (count - len(filtered_items_ids))} в отдел {depart_name}."
            )
            # перемещение (удаление) объектов со склада (учет всех переданных объектов не реализован)
        for key in [key for key in self.equipments if key in filtered_items_ids[:count + 1]]:
            del self.equipments[key]

    def __getitem__(self, key):
        if not isinstance(key, int):
            raise TypeError

        return self.equipments[key]


class OfficeEquipment(ABC):
    """Оргтехника"""
    oq_vendor: str
    oq_model: str
    oq_color: str
    oq_id: int = 0

    types_dict = {
        1: "ПРИНТЕР",
        2: "СКАНЕР",
        3: "КСЕРОКС"
    }

    def __init__(self, **kwargs):
        self.oq_vendor = kwargs["Производитель"]
        self.oq_model = self.oq_vendor + " " + kwargs["Модель"]
        self.oq_type = kwargs["Тип"]
        self.oq_color = kwargs["Цвет"]

        OfficeEquipment.oq_id += 1


class Printer(OfficeEquipment):
    """Принтер"""

    def __init__(self, **kwargs):
        super().__init__(oq_type="ПРИНТЕР", **kwargs)

    def __str__(self):
        return f"Принтер: {self.__dict__}"


class Scanner(OfficeEquipment):
    """Сканер"""

    def __init__(self, **kwargs):
        super().__init__(oq_type="СКАНЕР", **kwargs)

    def __str__(self):
        return f"Сканер: {self.__dict__}"


class Xerox(OfficeEquipment):
    """Ксерокс"""

    def __init__(self, **kwargs):
        super().__init__(oq_type="КСЕРОКС", **kwargs)

    def __str__(self):
        return f"Ксерокс: {self.__dict__}"


if __name__ == "__main__":
    result_list = []

    while True:
        items_dict = {
            "Тип": "",
            "Производитель": "",
            "Модель": "",
            "Цвет": "",
            "Количество": ""
        }
        print("Введите информацию о поступившем оборудовании\n")
        try:
            for key, value in items_dict.items():
                if key == "Тип":
                    user_input = UsefullMethodsClass.validate_digit_data("Выберете тип оборудования: 1 - Принтер; "
                                                                         "2 - Сканер; 3 - Ксерокс >> ")
                    items_dict[key] = OfficeEquipment.types_dict[user_input]
                elif key == "Количество":
                    user_input = UsefullMethodsClass.validate_digit_data("Введите количество (больше нуля): ")
                    items_dict[key] = user_input
                else:
                    user_input = UsefullMethodsClass.validate_str_data(f"{key}: ").upper()
                    items_dict[key] = user_input

            result_list.append(items_dict)

            user_choice = input("Для внесения информации о след. оборудовании нажмите Enter, иначе - 'stop' >> ")
            if user_choice == "stop":
                break
        except KeyboardInterrupt:
            print("\nРабота программы прекращена")
            exit(0)

    # прием на склад
    stock = Stock()

    try:
        for index, value in enumerate(result_list):
            if value["Тип"] == "ПРИНТЕР":
                for x in range(int(value["Количество"])):
                    temp_obj = Printer(**value)
                    stock.store(temp_obj)
            elif value["Тип"] == "СКАНЕР":
                for x in range(int(value["Количество"])):
                    temp_obj = Scanner(**value)
                    stock.store(temp_obj)
            elif value["Тип"] == "КСЕРОКС":
                for x in range(int(value["Количество"])):
                    temp_obj = Xerox(**value)
                    stock.store(temp_obj)

        dep, oq_type, oq_vendor, count = UsefullMethodsClass.validate_str_data("Введите отдел компании для "
                                                                               "передачи оборудования: "), \
                                         UsefullMethodsClass.validate_str_data("Введите тип передаваемого оборудования "
                                                                               "(принтер/сканер/ксерокс): "), \
                                         input("Введите производителя (enter - для пропуска): ").upper(), \
                                         UsefullMethodsClass.validate_digit_data("Введите кол-во оборудования "
                                                                                 "для передачи: ")
    except KeyboardInterrupt:
        print("\nРабота программы прекращена")
        exit(0)
    else:
        print(stock.transfer(dep, count, oq_type=oq_type.upper(), oq_vendor=oq_vendor.upper()))
