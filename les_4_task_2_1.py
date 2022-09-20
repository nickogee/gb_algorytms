'''
Написать два алгоритма нахождения i-го по счёту простого числа.
Функция нахождения простого числа должна принимать на вход натуральное и возвращать соответствующее простое число.
Проанализировать скорость и сложность алгоритмов.
'''

import cProfile

# адаптируем алгоритм "Решето Эратосфена", который был на 2 уроке под задачу


def erot_les_2(n):

    result = [2]

    # мы заранее не знаем, какой длины должен быть ряд натуральных чисел, чтобы в нем было n простых чисел,
    # по этому будем постепенно увеличивать ряд простых числел на шаг step,
    # пока в нем не будет содержаться n простых чисел
    step = 20

    def append_sieve(step):
        nonlocal result

        # последнее текущее значения ряда простых чисел и его индекс в списке result
        last = result[-1]
        last_ind = result.index(last, -1)

        # добавляемый ряд чисел
        add_list = [i for i in range(last + 1, last + step)]

        # максимальное число на текущей итерации
        max_int = add_list[-1]

        # расширим ряд простых чисел на добавочный ряд
        result = result + add_list

        # отсеивание непростых чисел
        # for i in range(1, last_ind + step):
        for i in result:
            # if result[i]:    # != None
            if i:    # != None
                # j = result[i] * 2
                j = i * 2
                while j <= max_int:
                    if result.count(j) > 0:
                        j_ind = result.index(j, last_ind)
                        result[j_ind] = None
                    # j += result[i]
                    j += i

        result = [i for i in result if i]
        return result

    while len(result) < n + 1:
        append_sieve(step)

    return result[n]


# print(erot_les_2(20))

# --------------------------------------------------------------------
# поиск 5-го простого числа: python3 -m timeit -n 1000 -s "import les_4_task_2_1" "les_4_task_2_1.erot_les_2(5)"
# 1000 loops, best of 5: 19.6 usec per loop

# поиск 10-го простого числа: python3 -m timeit -n 1000 -s "import les_4_task_2_1" "les_4_task_2_1.erot_les_2(10)"
# 1000 loops, best of 5: 62.8 usec per loop

# поиск 20-го простого числа: python3 -m timeit -n 1000 -s "import les_4_task_2_1" "les_4_task_2_1.erot_les_2(20)"
# 1000 loops, best of 5: 337 usec per loop

# поиск 40-го простого числа: python3 -m timeit -n 1000 -s "import les_4_task_2_1" "les_4_task_2_1.erot_les_2(40)"
# 1000 loops, best of 5: 1.87 msec per loop

# поиск 100-го простого числа: python3 -m timeit -n 1000 -s "import les_4_task_2_1" "les_4_task_2_1.erot_les_2(100)"
# 1000 loops, best of 5: 32.9 msec per loop

# --------------------------------------------------------------------

# cProfile.run('erot_les_2(5)')
# 20 {method 'count' of 'list' objects}

# cProfile.run('erot_les_2(10)')
# 64 {method 'count' of 'list' objects}

# cProfile.run('erot_les_2(20)')
# 362 {method 'count' of 'list' objects}

# cProfile.run('erot_les_2(40)')
# 1713 {method 'count' of 'list' objects}

# cProfile.run('erot_les_2(100)')
# 18429 {method 'count' of 'list' objects}
