'''
сортировка Шелла
'''

import random

size = 1000
array = [i for i in range(size)]

# перемешаем значения
random.shuffle(array)
print(array)


def shell_sort(array):
    assert len(array) < 40000, 'Массив слишком большой'

    def new_increment(array):

        inc = [1, 4, 10, 23, 57, 132, 301, 701, 1750]

        while len(array) <= inc[-1]:
            inc.pop()

        while len(inc) > 0:
            yield inc.pop()

    count = 0

    for increment in new_increment(array):
        for i in range(increment, len(array)):
            for j in range(i, increment -1, -increment):
                if array[j-increment] <= array[j]:
                    break
                array[j], array[j- increment] = array[j- increment], array[j]
                count += 1

    print(count)

shell_sort(array)
print(array)
