"""
6) Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный
предмет и наличие лекционных, практических и лабораторных занятий по этому предмету и их
количество. Важно, чтобы для каждого предмета не обязательно были все типы занятий.
Сформировать словарь, содержащий название предмета и общее количество занятий по
нему. Вывести словарь на экран.
Примеры строк файла: Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —
Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""

lessons_dict = {}

with open("sixth.txt", "r") as file:
    for el in file:
        lessons = el.split()
        name = lessons[0].rstrip(":")

        lessons_dict[name] = lessons[1:]

result = {}

for key, value in lessons_dict.items():
    result[key] = sum(
        [
            int(hours.split("(")[0])
            for hours in value
            if hours.split("(")[0].isdigit()
        ]
    )

print(result)
