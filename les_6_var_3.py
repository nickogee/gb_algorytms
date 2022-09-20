'''
Определить, какое число в массиве встречается чаще всего.
'''

from random import randint

# константа будет задавать длину начального массива
LS_LEN = 30

# констатнта будет задавать "правый" предел рандомных чисел
MAX_D = 10

# словарь будет содержать числа, и их количества в массиве {число: количество}
max_cnt_num = {}

ls = [randint(1, MAX_D) for i in range(1, LS_LEN + 1)]
print('Сгенерированный массив ', ls, sep='\n')

for i in ls:

    cnt = ls.count(i)
    # if cnt > max_cnt_num[i]:
    max_cnt_num[i] = cnt

max_key = [-1],
max_val = 0

for key, val in max_cnt_num.items():

    if val > max_val:
        max_val = val
        max_key = key


print(f'Наиболее часто в массиве встречается число {max_val} - {max_val} раз')

# ------------------------------------ используется словарь-------------------------------------
from les_6_meas import calc_memory

calc_memory(LS_LEN, MAX_D, max_cnt_num, max_val, max_key, ls)

# Значение "30" - 28 byte (<class 'int'>)
# Значение "10" - 28 byte (<class 'int'>)
# Значение "{8: 2, 7: 8, 5: 3, 3: 4, 6: 4, 10: 1, 9: 3, 4: 3, 1: 1, 2: 1}" - 360 byte (<class 'dict'>)
# Значение "8" - 28 byte (<class 'int'>)
# Значение "7" - 28 byte (<class 'int'>)
# Значение "[8, 7, 7, 5, 3, 3, 6, 6, 3, 5, 7, 10, 3, 9, 7, 5, 4, 7, 9, 6, 9, 7, 6, 7, 7, 1, 2, 4, 4, 8]"
#           - 312 byte (<class 'list'>)
# Общий размер используемой переменными памяти - 784

# ------------------------------------

# python:
# -v 3.9.13

# OS (MacOS):
# [Clang 6.0 (clang-600.0.57)] darwin
