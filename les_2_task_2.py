'''
Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
'''

# получим от пользователя число строкой
num = input('Введите первое число\n')

# инициируем счетчики
even = 0
even_st = ''

odd = 0
odd_st = ''

for i in num:

    if int(i)%2 == 0:
        even += 1
        even_st += f'{i} '
    else:
        odd += 1
        odd_st += f'{i} '

print(f' в числе {int(num)}: {even} четных ({even_st}) и {odd} не четных ({odd_st})' )


