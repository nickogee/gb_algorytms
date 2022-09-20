'''
сортировка пузырьком
'''

import random

size = 10
array = [i for i in range(size)]

# перемешаем значения
random.shuffle(array)
print(array)

n = 1
while n < len(array):
    for i in range(len(array) - n):

        if array[i] > array[i + 1]:
            array[i], array[i + 1] = array[i + 1], array[i]

    print(array)

    n += 1

print(array)
