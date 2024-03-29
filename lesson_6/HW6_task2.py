"""
2) Реализовать класс Road ( дорога), в котором определить атрибуты: length ( длина), width
(ширина). Значения данных атрибутов должны передаваться при создании экземпляра
класса. Атрибуты сделать защищенными. Определить метод расчета массы асфальта,
необходимого для покрытия всего дорожного полотна. Использовать формулу:
длина*ширина*масса асфальта для покрытия одного кв метра дороги асфальтом, толщиной в
1 см*число см толщины полотна. Проверить работу метода.
Например: 20м*5000м*25кг*5см = 12500 т
"""


class Road:
    _length = int
    _width = int

    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width

    def asphalt_mass(self):
        mass = int((self._length * self._width * 25 * 5) / 1000)
        print(f"Масса асфальта >>> {mass} т.")


res_mass = Road(int(input("Введите длину асфальта >>> ")), int(input("Введите ширину асфальта >>> ")))
res_mass.asphalt_mass()
