"""
1) Создать класс TrafficLight ( светофор) и определить у него один атрибут color ( цвет) и метод
running ( запуск). Атрибут реализовать как приватный. В рамках метода реализовать
переключение светофора в режимы: красный, желтый, зеленый. Продолжительность первого
состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый)
— на ваше усмотрение. Переключение между режимами должно осуществляться только в
указанном порядке (красный, желтый, зеленый). Проверить работу примера, создав экземпляр
и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении
выводить соответствующее сообщение и завершать скрипт.
"""

from time import sleep


class TrafficLight:
    __color = str

    def running(self):
        while True:
            start = input("Push 'Enter' for start/continue or 'q' for exit >>> ").lower()
            if start == "q":
                exit()
            else:
                try:
                    count = 1
                    while count < 4:
                        print(self.__color("\033[31m\033[1mRed"))
                        sleep(7)
                        print(self.__color("\033[33mYellow"))
                        sleep(2)
                        print(self.__color("\033[32mGreen"))
                        sleep(6)
                        count += 1

                except RuntimeError:
                    print("Нарушен режим работы светофора!")
                    exit()
                except AttributeError:
                    print("Нарушен режим работы светофора!")
                    exit()


lights = TrafficLight()

lights.running()
