"""
4) Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed,
color, name, is_police ( булево). А также методы: go, stop, turn(direction), которые должны
сообщать, что машина поехала, остановилась, повернула (куда). Опишите несколько
дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод
show_speed, который должен показывать текущую скорость автомобиля. Для классов
TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60
( TownCar ) и 40 ( WorkCar ) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к
атрибутам, выведите результат. Выполните вызов методов и также покажите результат.
"""


class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print("Машина поехала!")

    def move(self):
        print("Машина в движении!")

    def stop(self):
        print("Машина остановилась!")

    def turn_direction(self):
        print("Машина повернула направо!")

    def show_speed(self):
        print(f"Текущая скорость автомобиля >>> {self.speed} km/h")


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f"Текущая скорость >>> {self.speed} km/h!")
        if self.speed > 60:
            print("\33[31m\33[1mМашина движется с превышением скорости 60 км/ч!")


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f"Текущая скорость >>> {self.speed} km/h!")
        if self.speed > 40:
            print("\33[31m\33[1mМашина движется с превышением скорости 40 км/ч!")


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


police = PoliceCar(60, "Black", "Ford", True)
print(f"\33[33mПолицейский автомобиль >>> {police.name}, цвет >>> {police.color}")
police.go()
police.show_speed()
sport = SportCar(0, "Red", "Ferrari", False)
print(f"\33[31mCпорткар >>> {sport.name}, цвет >>> {sport.color}")
sport.stop()
sport.show_speed()

work = WorkCar(40, "Gray", "Isuzu", False)
print(f"\33[32mГрузовик >>> {work.name}, цвет >>> {work.color}")
work.turn_direction()
work.show_speed()

town = TownCar(100, "Blue", "Opel", False)
print(f"\33[36mСедан >>> {town.name}, цвет >>> {town.color}")
town.move()
town.show_speed()
