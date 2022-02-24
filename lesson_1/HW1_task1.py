"""
Задание 1.
Поработайте с переменными, создайте несколько. Выведите на экран
Запросите у пользователя несколько чисел и строк и сохраните в переменные. Выведите на экран.
"""

print("Hi, it's my first homework!")
name = "Igor"
age = 34
sex = "Male"
print("Меня зовут -", name)
print("Мой возраст -", age)
print("Мой пол -", sex)
user_name = input("Пожалуйста, введите Ваше имя >>> ")
user_surname = input("Теперь, Вашу фамилию >>> ")
user_age = int(input("Будьте добры, Ваш возраст >>> "))
while True:
    user_even_number = int(input("Введите любимое чётное число >>> "))
    if user_even_number % 2 == 0:
        break
while True:
    user_odd_number = int(input("Введите любимое нечётное число >>> "))
    if user_odd_number % 2 != 0:
        break
print("Итак. Вас зовут -", user_name, user_surname)
print("В свои", user_age, "вы любите следующие числа >>>", user_even_number, "и", user_odd_number)
print("WellDone!")
