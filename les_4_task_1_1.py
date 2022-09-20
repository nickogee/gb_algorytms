# возьмем задачу из ДЗ второго урока, изначально она была реализована как в примере ниже (с помощю рекурсии)

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


def rec_sum(n):

    if n == 1:
        return 1.0
    else:
        return 1.0 + (rec_sum(n-1)/(-2))


# тестирование функции
# test_fib(rec_sum)

# ------------------------------------

# для 5 чисел: python3 -m timeit -n 1000 -s"import les_4_task_1_1" "les_4_task_1_1.rec_sum(5)"
# 1000 loops, best of 5: 952 nsec per loop

# для 10 чисел: python3 -m timeit -n 1000 -s"import les_4_task_1_1" "les_4_task_1_1.rec_sum(10)"
# 1000 loops, best of 5: 2.37 usec per loop

# для 100 чисел: python3 -m timeit -n 1000 -s"import les_4_task_1_1" "les_4_task_1_1.rec_sum(100)"
# 1000 loops, best of 5: 21.5 usec per loop

# для 500 чисел: python3 -m timeit -n 1000 -s"import les_4_task_1_1" "les_4_task_1_1.rec_sum(500)"
# 1000 loops, best of 5: 125 usec per loop

# для 900 чисел: python3 -m timeit -n 1000 -s"import les_4_task_1_1" "les_4_task_1_1.rec_sum(900)"
# 1000 loops, best of 5: 232 usec per loop

# ------------------------------------------

# cProfile.run('rec_sum(5)')
# 8 function calls (4 primitive calls) in 0.000 seconds
# 5/1    0.000    0.000    0.000    0.000 les_4_task_1_1.py:20(rec_sum)

# cProfile.run('rec_sum(10)')
# 13 function calls (4 primitive calls) in 0.000 seconds
# 10/1    0.000    0.000    0.000    0.000 les_4_task_1_1.py:20(rec_sum)

# cProfile.run('rec_sum(100)')
# 103 function calls (4 primitive calls) in 0.000 seconds
# 100/1    0.000    0.000    0.000    0.000 les_4_task_1_1.py:20(rec_sum)

# cProfile.run('rec_sum(500)')
# 503 function calls (4 primitive calls) in 0.001 seconds
# 500/1    0.001    0.000    0.001    0.001 les_4_task_1_1.py:20(rec_sum)

# cProfile.run('rec_sum(900)')
# 903 function calls (4 primitive calls) in 0.001 seconds
# 900/1    0.001    0.000    0.001    0.001 les_4_task_1_1.py:20(rec_sum)


