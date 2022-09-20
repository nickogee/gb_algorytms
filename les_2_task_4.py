'''
Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,… Количество элементов (n) вводится с клавиатуры.
'''


def rec_sum(n):

    if n == 1:
        return 1
    else:
        return 1 + (rec_sum(n-1)/(-2))


n = int(input('Введите количество элементов n\n'))

print(f'Сумма элементов: {rec_sum(n)}')