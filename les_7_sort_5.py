'''
сортировка Хоара (быстрая сортировка)
'''

import random

size = 50
array = [i for i in range(size)]

# перемешаем значения
random.shuffle(array)
print(array)


def quick_sort(array):

    if len(array) <= 1:
        return array

    pivot = random.choice(array)
    s_ar = []
    m_ar = []
    l_ar = []

    for item in array:
        if item < pivot:
            s_ar.append(item)
        elif item > pivot:
            l_ar.append(item)
        elif item == pivot:
            m_ar.append(item)
        else:
            raise Exception('Непредвиденная ошибка')

    return quick_sort(s_ar) + m_ar + quick_sort(l_ar)


new_array = quick_sort(array)
print(new_array)
