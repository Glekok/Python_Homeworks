"""
2) Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная
сущность (класс) этого проекта — одежда, которая может иметь определенное название. К
типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют
параметры: размер ( для пальто) и рост ( для костюма) . Это могут быть обычные числа: V и
H , соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто
(V/6.5 + 0.5) , для костюма (2*H + 0.3) . Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке
знания: реализовать абстрактные классы для основных классов проекта, проверить на
практике работу декоратора @property .
"""

from abc import ABC, abstractmethod


class Clothes(ABC):
    coat = "Пальто"
    costume = "Костюм"

    def __init__(self, coat_size: float, costume_size: float):
        self.coat_size = coat_size
        self.costume_size = costume_size

    @abstractmethod
    def coat_fabrics(self):
        pass

    @abstractmethod
    def costume_fabrics(self):
        pass

    @abstractmethod
    def full_fabrics(self):
        pass


class Fabrics(Clothes):

    def coat_fabrics(self):
        return round((self.coat_size / 6.5 + 0.5), 2)

    def costume_fabrics(self):
        return round((self.costume_size * 2 + 0.3), 2)

    @property
    def full_fabrics(self):
        return f"Общий расход ткани >>> {self.coat_fabrics() + self.costume_fabrics()}"


f = Fabrics(44, 1.84)

print(f"Расход ткани на {Clothes.coat} >>> {f.coat_fabrics()}")
print(f"Расход ткани на {Clothes.costume} >>> {f.costume_fabrics()}")
print(f.full_fabrics)
