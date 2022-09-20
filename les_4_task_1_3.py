# попробуем оптимизировать работу функции с помощю мемоизации в список

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


def rec_sum_list(n):
    # базовый случай
    ls = [None] * 1000
    ls[:2] = [0, 1.0]

    def _find_sum(n):
        if ls[n] is None:
            ls[n] = 1.0 + (_find_sum(n - 1) / (-2))
        return ls[n]

    return _find_sum(n)


# тестирование функции
# test_fib(rec_sum_list)

# ------------------------------------

# для 5 чисел: python3 -m timeit -n 1000 -s "import les_4_task_1_3" "les_4_task_1_3.rec_sum_list(5)"
# 1000 loops, best of 5: 2.86 usec per loop

# для 10 чисел: python3 -m timeit -n 1000 -s "import les_4_task_1_3" "les_4_task_1_3.rec_sum_list(10)"
# 1000 loops, best of 5: 4.49 usec per loop

# для 100 чисел: python3 -m timeit -n 1000 -s "import les_4_task_1_3" "les_4_task_1_3.rec_sum_list(100)"
# 1000 loops, best of 5: 33.7 usec per loop

# для 500 чисел: python3 -m timeit -n 1000 -s "import les_4_task_1_3" "les_4_task_1_3.rec_sum_list(500)"
# 1000 loops, best of 5: 191 usec per loop

# для 900 чисел: python3 -m timeit -n 1000 -s "import les_4_task_1_3" "les_4_task_1_3.rec_sum_list(900)"
# 1000 loops, best of 5: 350 usec per loop

# ------------------------------------------

# cProfile.run('rec_sum_list(10)')
# 14 function calls (5 primitive calls) in 0.000 seconds
# 10/1    0.000    0.000    0.000    0.000 les_4_task_1_3.py:25(_find_sum)

# cProfile.run('rec_sum_list(100)')
# 104 function calls (5 primitive calls) in 0.000 seconds
# 100/1    0.000    0.000    0.000    0.000 les_4_task_1_3.py:25(_find_sum)

# cProfile.run('rec_sum_list(500)')
# 504 function calls (5 primitive calls) in 0.001 seconds
# 500/1    0.001    0.000    0.001    0.001 les_4_task_1_3.py:25(_find_sum)

# cProfile.run('rec_sum_list(900)')
# 904 function calls (5 primitive calls) in 0.002 seconds
# 900/1    0.002    0.000    0.002    0.002 les_4_task_1_3.py:25(_find_sum)


