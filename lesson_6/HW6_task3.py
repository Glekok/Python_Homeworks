"""
3) Реализовать базовый класс Worker ( работник), в котором определить атрибуты: name,
surname, position ( должность), income ( доход). Последний атрибут должен быть
защищенным и ссылаться на словарь, содержащий элементы: оклад и премия, например,
{"wage": wage, "bonus": bonus}. Создать класс Position ( должность) на базе класса Worker.
В классе Position реализовать методы получения полного имени сотрудника ( get_full_name) и
дохода с учетом премии ( get_total_income) . Проверить работу примера на реальных данных
(создать экземпляры класса Position , передать данные, проверить значения атрибутов,
вызвать методы экземпляров).
"""


class Worker:
    worker_count = 0

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}
        Worker.worker_count += 1


class Position(Worker):

    def get_full_name(self):
        return self.name + " " + self.surname + " >>> " + self.position

    def get_total_income(self):
        return sum(self._income.values())


full_data = Position("Ваня", "Жужнев", "Плотник 2-го разряда", 18567.55, 2000)
full_data_2 = Position("Жора", "Крепкий", "Грузчик", 11100, 800)
full_data_3 = Position("Гена", "Сытый", "Водитель Белаза", 22000, 3500)
print(full_data.get_full_name())
print(f"Зароботок с учетом премии составил >>> {full_data.get_total_income()} руб.")
print(full_data_2.get_full_name())
print(f"Зароботок с учетом премии составил >>> {full_data_2.get_total_income()} руб.")
print(full_data_3.get_full_name())
print(f"Зароботок с учетом премии составил >>> {full_data_3.get_total_income()} руб.")
print(f"Количество трудящихся >>> {Worker.worker_count} человек(а)")
