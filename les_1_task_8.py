'''
Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).
'''

# получим от пользователя три числа
a = int(input('Введите первое число\n'))     #\n для более удобного вида в консоли
b = int(input('Введите второе число\n'))
c = int(input('Введите третье число\n'))

if a > b > c or a < b < c:
    print(f'Среднее число - {b}')
elif b > a > c or b < a < c:
    print(f'Среднее число - {a}')
else:
    print(f'Среднее число - {c}')