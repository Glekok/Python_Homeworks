"""
Задание 4.
Пользователь вводит целое положительное число.
Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции.
"""

user_number = int(input("Введите любое положительное/целое число >>> "))
max_number = user_number % 10
while user_number >= 1:
    user_number //= 10
    # Для просмотра принципа работы >>> print(user_number)
    if user_number % 10 > max_number:
        max_number = user_number % 10
    if user_number > 9:
        continue
    else:
        print("Цифра - 'Босс' в Вашем числе >>>", max_number)
        break
