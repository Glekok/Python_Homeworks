"""
Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года
относится месяц (зима, весна, лето, осень). Напишите решения через list и через dict.
"""

calendar_dict = {"Winter": (1, 2, 12), "Spring": (3, 4, 5), "Summer": (6, 7, 8), "Autumn": (9, 10, 11)}
months_list = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
               "November", "December"]
user_choice = abs(int(input("Выберите месяц в числовом формате от 1 до 12 >>> ")))
for season, months in calendar_dict.items():
    if user_choice in months:
        print(f"{months_list[user_choice - 1]}. Время года >>> {season}")
