# попробуем оптимизировать работу функции с помощю цикла

'''
Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,… Количество элементов (n) вводится с клавиатуры.
'''

import cProfile


def test_fib(func):

    # список с суммами элементов, расчитан заранее
    ls = [1.0, 0.5, 0.75, 0.625, 0.6875, 0.65625, 0.671875, 0.6640625]

    for i in range(1, 9):
        assert ls[i-1] == func(i)
        print(f'Test {i} ok')


def rec_sum_cycle(n):
    # базовый случай
    if n == 1:
        return 1.0

    # будет накапливать сумму элементов
    summ = 1.0

    # будет содержать предыдущий элемент
    prev = 1.0

    for i in range(2, n + 1):
        summ += prev/(-2)
        prev = prev/(-2)

    return summ


# тестирование функции
# test_fib(rec_sum_cycle)

# ------------------------------------

# для 5 чисел: python3 -m timeit -n 1000 -s "import les_4_task_1_4" "les_4_task_1_4.rec_sum_cycle(5)"
# 1000 loops, best of 5: 1.13 usec per loop

# для 10 чисел: python3 -m timeit -n 1000 -s "import les_4_task_1_4" "les_4_task_1_4.rec_sum_cycle(10)"
# 1000 loops, best of 5: 1.73 usec per loop

# для 100 чисел: python3 -m timeit -n 1000 -s "import les_4_task_1_4" "les_4_task_1_4.rec_sum_cycle(100)"
# 1000 loops, best of 5: 14.2 usec per loop

# для 500 чисел: python3 -m timeit -n 1000 -s "import les_4_task_1_4" "les_4_task_1_4.rec_sum_cycle(500)"
# 1000 loops, best of 5: 74 usec per loop

# для 900 чисел: python3 -m timeit -n 1000 -s "import les_4_task_1_4" "les_4_task_1_4.rec_sum_cycle(900)"
# 1000 loops, best of 5: 139 usec per loop

# для 1000 чисел: python3 -m timeit -n 1000 -s "import les_4_task_1_4" "les_4_task_1_4.rec_sum_cycle(1000)"
# 1000 loops, best of 5: 152 usec per loop

# для 2000 чисел: python3 -m timeit -n 1000 -s "import les_4_task_1_4" "les_4_task_1_4.rec_sum_cycle(2000)"
# 1000 loops, best of 5: 316 usec per loop

# для 10000 чисел: python3 -m timeit -n 1000 -s "import les_4_task_1_4" "les_4_task_1_4.rec_sum_cycle(10000)"
# 1000 loops, best of 5: 1.59 msec per loop

# ------------------------------------------

# cProfile.run('rec_sum_cycle(10)')
# 4 function calls in 0.000 seconds
# 1    0.000    0.000    0.000    0.000 les_4_task_1_4.py:20(rec_sum_cycle)

# cProfile.run('rec_sum_cycle(100)')
# 4 function calls in 0.000 seconds
# 1    0.000    0.000    0.000    0.000 les_4_task_1_4.py:20(rec_sum_cycle)

# cProfile.run('rec_sum_cycle(500)')
# 4 function calls in 0.000 seconds
# 1    0.000    0.000    0.000    0.000 les_4_task_1_4.py:20(rec_sum_cycle)

# cProfile.run('rec_sum_cycle(900)')
# 4 function calls in 0.000 seconds
# 1    0.000    0.000    0.000    0.000 les_4_task_1_4.py:20(rec_sum_cycle)

# cProfile.run('rec_sum_cycle(2000)')
# 4 function calls in 0.000 seconds
# 1    0.000    0.000    0.000    0.000 les_4_task_1_4.py:20(rec_sum_cycle)

# cProfile.run('rec_sum_cycle(10000)')
# 4 function calls in 0.002 seconds
# 1    0.002    0.002    0.002    0.002 les_4_task_1_4.py:20(rec_sum_cycle)
