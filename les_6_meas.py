'''
модуль содержит функцию для замера количества используемой памяти
'''

import sys


def calc_memory(*args):

    mem_sum = 0
    for var in args:
        mem = sys.getsizeof(var)
        mem_sum += mem
        print(f'Значение "{var}" - {mem} byte ({var.__class__})')

    print(f'Общий размер используемой переменными памяти - {mem_sum}')


