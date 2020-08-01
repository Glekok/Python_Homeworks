"""
1. Создать список и заполнить его элементами различных типов данных.
Реализовать скрипт проверки типа данных каждого элемента.
Использовать функцию type() для проверки типа.
Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.
"""
my_list = [1, "hello", b"OMG! Bytes", 125, 2.4]

for element in my_list:
    print(f"{element} >>>", type(element))

print("________ NEXT LEVEL --------->")

"""
2. Для списка реализовать обмен значений соседних элементов, т.е.
Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input().
"""

result_list = input("Введите через пробел произвольные элементы списка >>> ").split()
print(result_list)
print(type(result_list))
element = 0
for elements in range(len(result_list) // 2):
    result_list[element], result_list[element + 1] = result_list[element + 1], result_list[element]
    element += 2
print(result_list)
print(type(result_list))

print("________ NEXT LEVEL --------->")

"""
3. Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года
относится месяц (зима, весна, лето, осень). Напишите решения через list и через dict.
"""

calendar_dict = {"Winter": (1, 2, 12), "Spring": (3, 4, 5), "Summer": (6, 7, 8), "Autumn": (9, 10, 11)}
months_list = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
               "November", "December"]
user_choice = abs(int(input("Выберите месяц в числовом формате от 1 до 12 >>> ")))
for season, months in calendar_dict.items():
    if user_choice in months:
        print(f"{months_list[user_choice - 1]}. Время года >>> {season}")

print("________ NEXT LEVEL --------->")

"""
4. Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое
слово с новой строки. Строки необходимо пронумеровать. Если слово длинное, выводить
только первые 10 букв в слове.
"""

user_line = input("Введите строку из нескольких слов, разделив их пробелами >>> ").split()
for ind, el in enumerate(user_line, 1):
    print(f"{ind} > {el[:10]}")

print("________ NEXT LEVEL --------->")

"""
5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
У пользователя необходимо запрашивать новый элемент рейтинга.
Если в рейтинге существуют элементы с одинаковыми значениями,
то новый элемент с тем же значением должен разместиться после них.
Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.

Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].
"""
my_list = [9, 8, 8, 7, 5, 4, 4, 2]
print(f"Работаем с данным рейтингом >>> {my_list}")
user_element = int(input("Введите любое целое число. Добавим его в рейтинг (0 = выход!) >>> "))
while user_element != 0:
    for element in range(len(my_list)):
        if my_list[element] is user_element:
            my_list.insert(element + 1, user_element)
            break
        elif user_element < my_list[-1]:
            my_list.append(user_element)
            break
        elif user_element > my_list[0]:
            my_list.insert(0, user_element)
            break
        elif my_list[element] > user_element > my_list[element + 1]:
            my_list.insert(element + 1, user_element)
            break
    print(f"Список теперь выглядит так >>> {my_list}")
    user_element = int(input("Введите любое целое число. Добавим его в рейтинг (0 = выход!) >>> "))

print("6 со '*' не успел осилить до конца!")
print(">>> FIN <<<")
