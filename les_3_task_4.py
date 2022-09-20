'''
Определить, какое число в массиве встречается чаще всего.
'''

from random import randint

# константа будет задавать длину начального массива
LS_LEN = 30

# констатнта будет задавать "правый" предел рандомных чисел
MAX_D = 10

# кортеж будет содержать число, которое чаще всего встречается и его количество в массиве (число, количество)
max_cnt_num = (0, 0)

ls = [randint(1, MAX_D) for i in range(1, LS_LEN + 1)]
print('Сгенерированный массив ', ls, sep='\n')

for i in ls:

    cnt = ls.count(i)
    if cnt > max_cnt_num[1]:
        max_cnt_num = (i, cnt)

print(f'Наиболее часто в массиве встречается число {max_cnt_num[0]} - {max_cnt_num[1]} раз')

