"""
3) Реализовать функцию my_func(), которая принимает три позиционных аргумента, и
возвращает сумму наибольших двух аргументов.
"""


def my_func(a, b, c):
    if a <= b <= c:
        return b + c
    elif b <= a <= c:
        return a + c
    else:
        return a + b


print(
    my_func(int(input('Введите число a >>> ')), int(input('Введите число b >>> ')), int(input('Введите число c >>> '))))
