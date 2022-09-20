'''
 Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
 заданный случайными числами на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.
'''

import random

size = 50
array = [random.randint(0, size) for i in range(30)]

print(array)


def merge_sort(array, start=0, end=len(array)):

    # начнем "делить" массив на подмассивы, пока в нем не останется по одному элементу
    if end - start > 1:
        mid = (start + end)//2
        merge_sort(array, start, mid)
        merge_sort(array, mid, end)

        # на этом этапе массив разбит, точнее получены индексы, которые нужо будет сравнивать для сортировки
        merge_list(array, start, mid, end)
    else:
        return


def merge_list(array, start, mid, end):
    left = array[start:mid]
    right = array[mid:end]
    k = start
    i = 0
    j = 0
    while (start + i < mid and mid + j < end):
        if (left[i] <= right[j]):
            array[k] = left[i]
            i = i + 1
        else:
            array[k] = right[j]
            j = j + 1
        k = k + 1
    if start + i < mid:
        while k < end:
            array[k] = left[i]
            i = i + 1
            k = k + 1
    else:
        while k < end:
            array[k] = right[j]
            j = j + 1
            k = k + 1


merge_sort(array)

print(array)