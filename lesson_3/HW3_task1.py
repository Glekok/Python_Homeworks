"""
1) Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их
деление. Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на
ноль.
"""


def division_numbers(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Деление на 0! ай-яй-яй)))")


print(division_numbers(int(input('Введите число a >>> ')), int(input('Введите число b >>> '))))
