'''
хэш-функции
сравнение строк с помощю хэширования
'''

import hashlib


def is_eq_str(a: str, b: str) -> bool:
    assert len(a) > 0 and len(b) > 0, 'Строки не могут быть пустыми'

    ha = hashlib.sha1(a.encode('utf-8')).hexdigest()
    hb = hashlib.sha1(b.encode('utf-8')).hexdigest()

    print(ha, hb, sep='\n')

    return ha == hb


s_1 = input('Введите строку 1\n')
s_2 = input('Введите строку 2\n')

print('Строки одинаковые' if is_eq_str(s_1, s_2) else 'Строки разные')

