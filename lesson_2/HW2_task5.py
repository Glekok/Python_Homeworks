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
