"""
7) Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное
значение. При вызове функции должен создаваться объект-генератор. Функция должна
вызываться следующим образом: for el in fact(n). Функция отвечает за получение факториала
числа, а в цикле необходимо выводить только первые n чисел, начиная с 1! и до n!.
Подсказка: факториал числа n — произведение чисел от 1 до n. Например, факториал
четырёх 4! = 1 * 2 * 3 * 4 = 24.
"""

from itertools import count
from math import factorial


def fact():
    for el in count(1):
        yield factorial(el)


my_gen = fact()
print(my_gen)

try:
    n = int(input("Введите предельное число генератора >>> "))

    counter = 1
    for element in fact():
        if counter <= abs(n):
            print(f"{counter}! = {element}")
            counter += 1
        else:
            break
except ValueError:
    print("Need only integers!")
    exit()
