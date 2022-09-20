'''
Пользователь вводит данные о количестве предприятий,
их наименования и прибыль за четыре квартала для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий) и отдельно вывести наименования предприятий,
чья прибыль выше среднего и ниже среднего.
'''

from collections import namedtuple, OrderedDict

# русские и английские названия характеристик компаний заведем в константу, чтобы не переписывать
PROPERTYS_RU = ['Наименование', 'Годовая прибыль']
PROPERTYS_EN = ['name', 'profit']

# будет заполняться компаниями
dct = {}

# для обращения к свойствам по имени будем использовать английские слова
Company = namedtuple('Company', PROPERTYS_EN)

comp_count = int(input('Укажите количество компаний\n'))

# сумма прибылей всех компаний, для расчета средней прибыли
profit_sum = 0

for i in range(1, comp_count + 1):
    curr_name = input(f'Введите {PROPERTYS_RU[0]} компании №{i}\n')
    curr_sum = float(input(f'Введите {PROPERTYS_RU[1]} компании №{i}\n'))

    curr_comp = Company(curr_name, curr_sum)
    profit_sum += curr_sum
    dct[i] = curr_comp

# средняя прибыль по компаниям
avg_profit = round(profit_sum/comp_count, 2)

print(f'Средняя прибыль компаний - {avg_profit}')

# список компаний, чьи прибыли выше средней
h_list = []

# список компаний, чьи прибыли ниже средней
l_list = []

for cmp in dct.values():
    if cmp.profit > avg_profit:
        h_list.append(cmp.name)
    else:
        l_list.append(cmp.name)

print(f'Комании, прибыль которых ниже средней - {l_list}')
print(f'Комании, прибыль которых выше средней - {h_list}')









