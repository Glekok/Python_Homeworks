"""
7) Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая
строка должна содержать данные о фирме: название, форма собственности, выручка,
издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также
среднюю прибыль. Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а
также словарь со средней прибылью. Если фирма получила убытки, также добавить ее в
словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{ "firm_1" : 5000 , "firm_2" : 3000 , "firm_3" : 1000 }, { "average_profit" : 2000 }]
Подсказка: использовать менеджер контекста.
"""

import json

income_dict = {}
profit_list = []
finally_list = []

with open("seventh.txt", "r") as main_file:
    content = main_file.readlines()

    for el in content:
        profit = int(el.split()[2]) - int(el.split()[3])
        income_dict.setdefault(el.split()[0], profit)
        profit_list.append(profit)
        if profit > 0:
            average_profit = round(sum(map(float, profit_list)) / len(profit_list), 2)
        avg_dict = {"average_profit": average_profit}

    finally_list.append(income_dict)
    finally_list.append(avg_dict)

    print(f"Итоговый список >>> {finally_list}")

with open("seventh.json", "w+") as my_json_file:
    json.dump(finally_list, my_json_file)

    json_str = json.dumps(finally_list)
    print(f"Содержимое файла .json >>> {json_str}")
