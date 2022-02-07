"""
4) Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно
данные. При этом английские числительные должны заменяться на русские. Новый блок строк
должен записываться в новый текстовый файл.
"""
new_strings = []
translate = ["Один", "Два", "Три", "Четыре"]
with open("fourth.txt", "r") as file:
    x = 0
    for el in file:
        el = el.split(" ", 1)
        new_strings.append(translate[x] + ' ' + el[1])
        x += 1
    print(new_strings)

with open("fourth_rus.txt", "w") as file_2:
    file_2.writelines(new_strings)
