"""
5) Программа запрашивает у пользователя строку чисел, разделенных пробелом. При нажатии
Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел,
разделенных пробелом и снова нажать Enter. Сумма вновь введенных чисел будет
добавляться к уже подсчитанной сумме. Но если вместо числа вводится специальный символ,
выполнение программы завершается. Если специальный символ введен после нескольких
чисел, то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого
завершить программу.
"""


def sum_func():
    main_sum = 0
    user_quit = False
    while not user_quit:
        try:
            user_list = input("Вводите числа через пробел, в конце нажав Enter (q == exit) >>> ").lower().split()

            moment_sum = 0
            for element in range(len(user_list)):
                if user_list[element] == "q":
                    user_quit = True
                    break
                else:
                    moment_sum = moment_sum + int(user_list[element])

            main_sum = main_sum + moment_sum

            print(f"На данный момент сумма элементов >>> {main_sum}")
        except ValueError:
            print(">>> Нужны числа! Либо 'q' для выхода <<<")
    print(f"Итоговая сумма >>> {main_sum}")


sum_func()
