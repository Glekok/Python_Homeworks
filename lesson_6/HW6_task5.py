"""
5) Реализовать класс Stationery ( канцелярская принадлежность). Определить в нем атрибут title
(название) и метод draw ( отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать
три дочерних класса Pen ( ручка), Pencil ( карандаш), Handle ( маркер). В каждом из классов
реализовать переопределение метода draw. Для каждого из классов метод должен выводить
уникальное сообщение. Создать экземпляры классов и проверить, что выведет описанный
метод для каждого экземпляра.
"""


class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print("\33[32m\33[1mЗапуск отрисовки!")


class Pen(Stationery):
    def __init__(self, title="Ручка"):
        super().__init__(title)

    def draw(self):
        print(f"\33[30m{self.title} рисует круг...")


class Pencil(Stationery):
    def __init__(self, title="Карандаш"):
        super().__init__(title)

    def draw(self):
        print(f"\33[34m{self.title} рисует квадрат...")


class Handle(Stationery):
    def __init__(self, title="Маркер"):
        super().__init__(title)

    def draw(self):
        print(f"\33[35m{self.title} закрашивает фигуры...")


stationery = Stationery("Канцелярская принадлежность")
stationery.draw()
pen = Pen()
pen.draw()
pencil = Pencil()
pencil.draw()
handle = Handle()
handle.draw()
