"""
1) Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде
строки формата «день-месяц-год». В рамках класса реализовать два метода. Первый, с
декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к
типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа,
месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на
реальных данных.
"""


class Date:
    user_date = str

    def __init__(self, user_date: str):
        self.user_date = user_date

    @classmethod
    def convert(cls, user_date):

        for el in user_date.split("-"):
            if el != "-":
                res_date.append(int(el))
        return res_date

    def __str__(self):
        return f"Дата разбитая на числа >>> {Date.convert(self.user_date)}"

    @staticmethod
    def valid():
        if 1 <= res_date[0] <= 31 and 1 <= res_date[1] <= 12 and res_date[2] <= 2020:
            return f"\033[32m\033[1mДата верна!"
        else:
            return f"\033[31m\033[1mНеверно указана дата!"


res_date = []
d = Date("30-08-2020")
print(d)
print(Date.valid())
