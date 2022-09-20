'''
Написать два алгоритма нахождения i-го по счёту простого числа.
Функция нахождения простого числа должна принимать на вход натуральное и возвращать соответствующее простое число.
Проанализировать скорость и сложность алгоритмов.
'''

import cProfile
from itertools import count

# реализуем классический способ проверки числа на простоту

def classic_prime(n):

    def prime_num(num):
        d = 2
        while num % d != 0:
            d += 1
        return d == num

    # здесь мы "запустим" бесконейный ряд простых чисел, и когда найдем n-ое простое число остновим генегацию ряда
    # и вернем нужное простое число

    # счетчик найденных простых чисел
    prime_count = 0
    target = 0

    # сразу вернем 2 если нужно первое простое число
    if n == 1:
        return 2

    for el in count(2):

        if prime_num(el):
            prime_count += 1

        if prime_count == n:
            target = el
            break

    return target


# print(classic_prime(40))

# --------------------------------------------------------------------
# поиск 5-го простого числа: python3 -m timeit -n 1000 -s "import les_4_task_2_2" "les_4_task_2_2.classic_prime(5)"
# 1000 loops, best of 5: 4.69 usec per loop

# поиск 10-го простого числа: python3 -m timeit -n 1000 -s "import les_4_task_2_2" "les_4_task_2_2.classic_prime(10)"
# 1000 loops, best of 5: 17.2 usec per loop

# поиск 20-го простого числа: python3 -m timeit -n 1000 -s "import les_4_task_2_2" "les_4_task_2_2.classic_prime(20)"
# 1000 loops, best of 5: 68.7 usec per loop

# поиск 40-го простого числа: python3 -m timeit -n 1000 -s "import les_4_task_2_2" "les_4_task_2_2.classic_prime(40)"
# 1000 loops, best of 5: 295 usec per loop

# поиск 100-го простого числа: python3 -m timeit -n 1000 -s "import les_4_task_2_2" "les_4_task_2_2.classic_prime(100)"
# 1000 loops, best of 5: 2.17 msec per loop

# --------------------------------------------------------------------

# cProfile.run('classic_prime(5)')
# 10 les_4_task_2_2.py:14(prime_num)

# cProfile.run('classic_prime(10)')
# 28 les_4_task_2_2.py:14(prime_num)

# cProfile.run('classic_prime(20)')
# 70 les_4_task_2_2.py:14(prime_num)

# cProfile.run('classic_prime(40)')
# 172 les_4_task_2_2.py:14(prime_num)

cProfile.run('classic_prime(100)')
# 540 les_4_task_2_2.py:14(prime_num)






