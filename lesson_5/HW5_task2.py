"""
2) Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить
подсчет количества строк, количества слов в каждой строке.
"""

file = open("second.txt", "r")

content = file.readlines()

print(f"{content} Строк в файле >>> {len(content)}")

file.close()

file = open("second.txt", "r")

content = file.readlines()
i = 0
string = 1
for el in content:
    print(f"Количество слов в {string}-й строке >>> {len(content[i].split())}")
    i += 1
    string += 1

file.close()
