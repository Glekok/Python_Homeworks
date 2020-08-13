"""
1) Создать программно файл в текстовом формате, записать в него построчно данные,
вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.
"""

with open("first.txt", "w", encoding="utf-8") as file:
    text = input("Введите содержимое файла >>> ")
    while text:
        if text:
            file.writelines(text + "\n")
            text = input("Дополните содержимое файла или жми Enter для завершения ввода >>> ")
        else:
            break
file = open(r"first.txt")
for line in file.readlines():
    print(line.replace("\n", ""))
file.close()
