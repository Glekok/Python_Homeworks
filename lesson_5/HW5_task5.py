"""
5) Создать (программно) текстовый файл, записать в него программно набор чисел,
разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить
ее на экран.
"""
try:
    with open("fifth.txt", "w", encoding="utf-8") as file:
        numbers = input("Вводите числа через пробел, затем жми Enter >>> ").split()

        for el in numbers:
            file.writelines(el + "\n")
        print(f"Сумма введённых чисел >>> {sum(map(float, numbers))}")
except ValueError:
    print("Input Error! Only int or float")
except IOError:
    print("Something went wrong!")
