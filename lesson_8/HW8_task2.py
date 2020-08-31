"""
2) Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля в
качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с
ошибкой.
"""


class ZeroDivision(Exception):
    def __init__(self, text):
        self.txt = text


while True:
    dividend = float(input("Веедите делимое >>> "))
    divider = float(input("Введите делитель >>> "))

    try:
        if divider == 0:
            raise ZeroDivision("Попытка деления на 0! Выход из программы...")
    except ZeroDivision as err:
        print(err)
        break
    else:
        res = round((dividend / divider), 2)
        print(f"Ваш результат >>> {res}")
