'''
Отсортируйте по убыванию методом пузырька одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы.
'''

import random

size = 20
array = [random.randint(-size, size) for i in range(30)]

print(array)

# введем переменную, в которой будет храниться последнее отсортированное число (то есть текущее минимальное)
min_el = - size - 1

cnt = 0
n = 1
while n < len(array):
    for i in range(len(array) - n):

        # если текужее число в массиве равно или на единицу меньше текущего минимального,
        # сразу "телепортируем" его на место, с индексом на 1 меньше,
        # запоминаем это число  как текущее минимальное и прерываем внутренний цикл
        if array[i] == min_el or array[i] == (min_el - 1):
            array[i], array[len(array) - n] = array[len(array) - n], array[i]
            min_el = array[len(array) - n]
            cnt += 1
            break

        if array[i] < array[i + 1]:
            array[i], array[i + 1] = array[i + 1], array[i]

        # каждый раз, когда упорядовачеется текущее минимальное число, будем его ложить в переменную
        if i == (len(array) - n - 1):
            min_el = array[i + 1]

    n += 1

print(array)
print(cnt)

