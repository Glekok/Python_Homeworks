"""
Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое
слово с новой строки. Строки необходимо пронумеровать. Если слово длинное, выводить
только первые 10 букв в слове.
"""

user_line = input("Введите строку из нескольких слов, разделив их пробелами >>> ").split()
for ind, el in enumerate(user_line, 1):
    print(f"{ind} > {el[:10]}")