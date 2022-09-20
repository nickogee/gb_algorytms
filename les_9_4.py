'''
хэш-функции
поиск подстроки в строке с помощю хэширования
'''

import hashlib


def Rabin_Karp(s: str, subs:str) -> int:
    assert len(s) > 0 and len(subs) > 0, 'Строки не могут быть пустыми'
    assert len(s) >= len(subs), 'Подстрока короче строки'

    len_sub = len(subs)
    h_sub = hashlib.sha1(subs.encode('utf-8')).hexdigest()

    for i in range(len(s) - len_sub + 1):

        if h_sub == hashlib.sha1(s[i: i + len_sub].encode('utf-8')).hexdigest():
            if s[i: i + len_sub] == subs:
                return i

    return -1


s_1 = input('Введите строку 1\n')
s_2 = input('Введите подстроку для поиска 2\n')

pos = Rabin_Karp(s_1, s_2)
print(pos)
