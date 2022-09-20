'''
сортировка Хоара (быстрая сортировка)
вариант без использования дополнительной памяти
'''

import random

size = 10
array = [i for i in range(size)]

# перемешаем значения
random.shuffle(array)
print(array)


def revers(array):
    for i in range(len(array) // 2):

        # замена зеркально расположенных элементов относительно середины массива
        array[i], array[len(array) - i - 1] = array[len(array) - i - 1], array[i]


revers(array)
print(array)
