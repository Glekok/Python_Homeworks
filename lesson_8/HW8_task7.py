"""
7) Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное
число», реализуйте перегрузку методов сложения и умножения комплексных чисел.
Проверьте работу проекта, создав экземпляры класса (комплексные числа) и выполнив
сложение и умножение созданных экземпляров. Проверьте корректность полученного
результата.
"""


class ComplexNumbers:
    x: int
    y: int

    def __init__(self, user_list: tuple):
        self.x = user_list[0]
        self.y = user_list[1]

    def __add__(self, other):
        return ComplexNumbers((self.x + other.x, self.y + other.y))

    def __mul__(self, other):
        x_res = self.x * other.x + (
            self.y * other.y * -1 if self.y != 0 and other.y != 0 else self.y * other.y)
        y_res = self.x * other.x + self.y * other.y

        return ComplexNumbers((x_res, y_res))

    def __str__(self):
        output = ''
        if self.x != 0:
            output += str(self.x)

        if self.y != 0:
            if self.y != 0 and self.y > 0:
                output += '+'

            if self.y == 1:
                output += 'i'
            elif self.y == -1:
                output += '-i'
            else:
                output += str(self.y) + 'i'

        return output


num_1 = ComplexNumbers((8, 8))
num_2 = ComplexNumbers((21, -1))
print(f"cn_1 >>> {num_1}\ncn_2 >>> {num_2}")
print(f"Результат сложения = {num_1 + num_2}")
print(f"Результат умножения = {num_1 * num_2}")
