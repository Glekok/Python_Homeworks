"""
4) Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А
также класс «Оргтехника», который будет базовым для классов-наследников. Эти классы —
конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом классе определить
параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
уникальные для каждого типа оргтехники.

5) Продолжить работу над первым заданием. Разработать методы, отвечающие за приём
оргтехники на склад и передачу в определенное подразделение компании. Для хранения
данных о наименовании и количестве единиц оргтехники, а также других данных, можно
использовать любую подходящую структуру, например словарь.

6) Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых
пользователем данных. Например, для указания количества принтеров, отправленных на
склад, нельзя использовать строковый тип данных.

Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники»
максимум возможностей, изученных на уроках по ООП.
"""


class OfficeEquipment:
    name: str
    price: float

    def __init__(self, name, price):
        self.name = name
        self.price = price


class WrongValue(Exception):
    def __str__(self):
        return f"\033[31m\033[1mFatal error! Need a number for added!"


class OfficeStock:
    current_count: int
    max_count: int
    equipment: dict

    def __init__(self, count):
        self.current_count = 0
        self.max_count = count
        self.equipment = {}

    @staticmethod
    def checking(item_amount):
        if type(item_amount) != int:
            raise WrongValue
        else:
            return int(item_amount)

    def completing(self, item_type: OfficeEquipment, item_amount: int):
        try:
            self.current_count += self.checking(item_amount)
            print(f"You added {item_amount} item(s). {self.max_count - self.current_count} free space(s) left.")
            if item_type in self.equipment:
                self.equipment[item_type] += item_amount
            else:
                self.equipment[item_type] = item_amount

        except WrongValue as value:
            print(value)

    def __str__(self):
        return str('\n'.join(
            [f"{i.__class__.__name__} {i.name}, цена: {i.price}, количество: {j}." for i, j in
             self.equipment.items()]) + '\n')


class Printer(OfficeEquipment):
    _vendor_code: int

    def __init__(self, name: str, price: float, vendor_code: int):
        super().__init__(name, price)
        self._vendor_code = vendor_code

    def __str__(self):
        return f">>> Артикул: {self._vendor_code}"


class Scanner(OfficeEquipment):
    _vendor_code: int

    def __init__(self, name: str, price: float, vendor_code: int):
        super().__init__(name, price)
        self._vendor_code = vendor_code

    def __str__(self):
        return f">>> Артикул: {self._vendor_code}"


class Xerox(OfficeEquipment):
    _vendor_code: int

    def __init__(self, name: str, price: float, vendor_code: int):
        super().__init__(name, price)
        self._vendor_code = vendor_code

    def __str__(self):
        return f">>> Артикул: {self._vendor_code}"


p = Printer("Canon", 5000, 125568)
s = Scanner("ASUS", 6500, 125569)
x = Xerox("Genius", 8888.88, 125570)
ss = Scanner("DEXP", 4400, 125777)

stock = OfficeStock(7)
stock.completing(p, 1)
print(p)

stock.completing(s, 2)
print(s)

stock.completing(x, 3)
print(x)

stock.completing(ss, "1")

print(f"\033[0m\033[34m\033[1mAdded items:\n{stock}")
