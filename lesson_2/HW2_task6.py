"""
6. *Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
Каждый кортеж хранит информацию об отдельном товаре.
В кортеже должно быть два элемента — номер товара и словарь с параметрами
(характеристиками товара: название, цена, количество, единица измерения).
Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
Пример готовой структуры:
[
    (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
    (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
    (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
]
Необходимо собрать аналитику о товарах.
Реализовать словарь, в котором каждый ключ — характеристика товара, например название,
а значение — список значений-характеристик, например список названий товаров.
Пример:
{
“название”: [“компьютер”, “принтер”, “сканер”],
“цена”: [20000, 6000, 2000],
“количество”: [5, 2, 7],
“ед”: [“шт.”]
}
"""

products = {
    "Name": str,
    "Price": int,
    "Amount": int,
    "Units": str,
}

product_list = []
product_counter = 1

while True:
    choice = input(f"Now in list {len(product_list)} products, would you like to add any? (y/n) >>> ").lower()
    if choice == "n":
        break
    else:
        product_info = {}

        for property_name, property_type in products.items():
            user_choice = input(f"Input {property_name} >>> ")
            product_info[property_name] = property_type(user_choice)
        product_list.append((product_counter, product_info))
        product_counter += 1

# print(product_list)

analytics = {}

for analytics_key in products.keys():
    item_list = []

    for product in product_list:
        item_list.append(product[1][analytics_key])

    analytics[analytics_key] = item_list

print(analytics)
