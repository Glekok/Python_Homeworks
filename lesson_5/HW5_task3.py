"""
3) Создать текстовый файл (не программно), построчно записать фамилии сотрудников и
величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода
сотрудников.
Пример файла:
Иванов 23543.12
Петров 13749.32
"""

file = open("third.txt", "r")

income = []
content = file.readlines()
print("Оклад менее 20тыс.руб у следующих сотрудников:")
for el in content:
    income.append(el.split()[1])
    if float(el.split()[1]) < 20000.00:
        print(f" >>> {el.split()[0]}")

print(f"Средний доход по сотрудникам составляет >>> {sum(map(float, income)) / len(content)}")

file.close()
