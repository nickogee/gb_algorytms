'''
Определение количества различных подстрок с использованием хеш-функции. Пусть на вход функции дана строка.
Требуется вернуть количество различных подстрок в этой строке
'''

import hashlib


def substring_count(s: str)-> int:
    assert len(s) > 0, 'Строка не может быть пустой'

    # множество будет собирать генегируемые хэши
    hash_set = set()

    # создадим свой генератор, с Блэкджеком и подстроками,
    # которые будут выдоваться в зависимости от нужной длины подстроки
    def substring_generator(s: str, l_sub: int):

        start_ind = 0
        while start_ind + l_sub - 1 < len(s):
            cur_sub = s[start_ind: start_ind + l_sub]
            start_ind += 1
            yield cur_sub

    # константа, будет задавать длину подстроки
    l_sub = 1

    while l_sub < len(s):

        # мнициируем генератор для текущей длины подстроки
        gen = substring_generator(s, l_sub)

        for sub_s in gen:

            # вычисляем хэш подстроки и ложим (кладем) его в множество
            # соответственно все хэши будут уникальны
            h_sub = hashlib.sha1(sub_s.encode('utf-8')).hexdigest()
            hash_set.add(h_sub)

        # увеличиваем длину подстроки и повторяем
        l_sub += 1

    return len(hash_set)


s_1 = input('Введите строку\n')

print(f' Количество возможных уникальных подстрок в строке {s_1} - {substring_count(s_1)}')
