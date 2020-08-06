"""
1) Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной
платы сотрудника. В расчете необходимо использовать формулу: (выработка в часах*ставка в
час) + премия. Для выполнения расчета для конкретных значений необходимо запускать
скрипт с параметрами.
"""
# Привет. Запускаю данный скрипт с параметрами! Правая кнопка >>> edit {file_name} >>> parameters заполняю через пробел!

from sys import argv


def hello(name):
    print(f"Hello, {name}")


def calculate():
    try:
        file, rate, time, bonus = argv
        salary = int(rate) * float(time) + int(bonus)
        print(f"Your salary >>> {salary} $")
    except ValueError:
        print("Invalid args")
        exit()


hello("Worker!")
calculate()
