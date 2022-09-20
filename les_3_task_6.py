'''
В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.
'''

from random import randint

# константа будет задавать длину начального массива
LS_LEN = 20

# констатнта будет задавать "правый" предел рандомных чисел
MAX_D = 50

# кортеж будет содержать максимальный элемент и его индекс (индекс, элемент)
max_el = (0, 0)

# кортеж будет содержать минимальный элемент и его индекс (индекс, элемент)
min_el = (0, MAX_D + 1)

ls = [randint(1, MAX_D) for i in range(1, LS_LEN + 1)]
print('Сгенерированный массив ', ls, sep='\n')

# найдем индексы максимального и минимального эл-ов
for ind, el in enumerate(ls):

    if el > max_el[1]:
        max_el = (ind, el)

    if el < min_el[1]:
        min_el = (ind, el)

# получим срез между этими элементами
if max_el[0] > min_el[0]:
    ls_cut = ls[min_el[0] + 1 : max_el[0]]
else:
    ls_cut = ls[max_el[0] + 1 : min_el[0]]

summ = 0
for i in ls_cut:
    summ += i

print(f'Сумма элементов между {min_el[1]} и {max_el[1]} - {summ}')
