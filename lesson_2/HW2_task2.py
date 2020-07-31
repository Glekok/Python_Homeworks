"""
Для списка реализовать обмен значений соседних элементов, т.е.
Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input().
"""

result_list = input("Введите через пробел произвольные элементы списка >>> ").split()
print(result_list)
print(type(result_list))
element = 0
for elements in range(len(result_list) // 2):
    result_list[element], result_list[element + 1] = result_list[element + 1], result_list[element]
    element += 2
print(result_list)
print(type(result_list))
