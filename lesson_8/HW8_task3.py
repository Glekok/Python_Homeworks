"""
3) Создайте собственный класс-исключение, который должен проверять содержимое списка на
наличие только чисел. Проверить работу исключения на реальном примере. Необходимо
запрашивать у пользователя данные и заполнять список только числами. Класс-исключение
должен контролировать типы данных элементов списка.

Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно, пока
пользователь сам не остановит работу скрипта, введя, например, команду “stop”. При этом
скрипт завершается, сформированный список с числами выводится на экран.

Подсказка: для данного задания примем, что пользователь может вводить только числа и
строки. При вводе пользователем очередного элемента необходимо реализовать проверку
типа элемента и вносить его в список, только если введено число. Класс-исключение должен
не позволить пользователю ввести текст (не число) и отобразить соответствующее
сообщение. При этом работа скрипта не должна завершаться.
"""


class NoTextInList(Exception):
    @staticmethod
    def checking(user_choice, res_list: list):
        try:
            res_list.append(int(user_choice))
            return res_list
        except ValueError:
            if user_choice != 'q':
                print("Need a number!")


user_list = []
user_quit = False
while not user_quit:
    user_in = input("Введите число для формирования списка (q == exit) >>> ").lower()
    if user_in == 'q':
        user_quit = True
        break
    NoTextInList.checking(user_in, user_list)

print(f"Attention! Ваш список >>> {user_list}")
