'''
Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив, элементы которого — цифры числа.
'''


# определим класс для шестнадцатиразрядных чисел
class Hex_num:

    # класс содержит соответствие между шестнадцатиричным и десятиричным числом
    hex_map = {
        '0': 0,
        '1': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        'A': 10,
        'B': 11,
        'C': 12,
        'D': 13,
        'E': 14,
        'F': 15
    }

    num_list = []

    def __init__(self, num_str):

        # при инициализакии числа проверим на корректность введенные символы
        if self.correct_symbol(num_str):

            # список символов, составляющих число будет храниться в свойстве экземпляра
            self.num_list = [i.upper() for i in num_str]

    def correct_symbol(self, num_str):
        err = False
        for i in num_str:

            if i not in self.hex_map.keys():
                print(f' В числе {num_str} не корректный символ {i}')
                err = True

        return not err

    def get_key_of_value(self, n_res):
        for key, val in Hex_num.hex_map.items():
            if val == n_res:
                return key

    # актуальность числа будет определяться наличием непустого списка символов
    def __bool__(self):
        return bool(self.num_list)

    def __len__(self):
        return len(self.num_list)

    def __str__(self):
        st = ''
        for i in self.num_list:
            st += i
        return st + '(hex)'

    def __add__(self, other):
        # будет содержать строку с результатом
        result_str = ''

        # найдем максимальное и минималное по длине списка число
        # для этого переопределен метод __len__()
        if len(self) != len(other):
            max_num, min_num = max(self, other, key=len), min(self, other, key=len)

            # выровним списки по длине, добавив к меньшему нули
            add_zero_ls = ['0'] * (len(max_num) - len(min_num))
        else:
            max_num, min_num = self, other
            add_zero_ls = []

        # итерироваться будем по перевернутым спискам для удобства
        max_list_r = max_num.num_list[::-1]
        min_list_r = min_num.num_list[::-1] + add_zero_ls

        # признак увеличения следующего разряда ("в уме")
        on_mind = 0

        for i in range(0, max_num.__len__()):

            # получим десятичные значения цифр
            n_1 = Hex_num.hex_map[max_list_r[i]]
            n_2 = Hex_num.hex_map[min_list_r[i]]

            # результат - остаток от деления суммы цифр + "что в уме" на 16
            n_res = (int(n_1) + int(n_2) + on_mind) % 16

            # сбрасываем увеличение разряда после применения
            on_mind = 0

            # если сумма цифр была больше 15 - запоминаем 1 "в уме"
            if n_1 + n_2 >= 15:
                on_mind = 1

            # найдем ключ по полученному значению и добавим его в строку-результат (пока что перевернутый)
            result_str += self.get_key_of_value(n_res)

        if on_mind:
            result_str += self.get_key_of_value(on_mind)

        return Hex_num(result_str[::-1])

    def __mul__(self, other):

        # найдем максимальное и минималное по длине списка число
        # для этого переопределен метод __len__()
        if len(self) != len(other):
            max_num, min_num = max(self, other, key=len), min(self, other, key=len)
        else:
            max_num, min_num = self, other

        # итерироваться будем по перевернутым спискам для удобства
        max_list_r = max_num.num_list[::-1]
        min_list_r = min_num.num_list[::-1]

        # признак увеличения следующего разряда ("в уме")
        on_mind = 0

        # здесь будут собераться все списки, полученные перемножением элементов
        to_add_ls = []

        for ind, val in enumerate(min_list_r):

            # заполнение нулями начала списка старших разрядов
            result_ls = [] + (['0'] * ind)

            n_1 = Hex_num.hex_map[val]

            for i in max_list_r:

                # получим десятичные значения цифр
                n_2 = Hex_num.hex_map[i]

                n_res = ((int(n_1) * int(n_2)) + on_mind) % 16

                on_mind = ((int(n_1) * int(n_2)) + on_mind) // 16

                result_ls.append(self.get_key_of_value(n_res))

            # добавляем в конец нули в зависимости от "младшенства" разряда
            result_ls = result_ls + (['0'] * (len(min_list_r) -1 - ind))

            to_add_ls.append(result_ls)

        # если у нас осталось значение "в уме", добавляем его как старший разряд в последний список
        # и расширяем все предыдущие списки на один "0"
        if on_mind:
            to_add_ls[-1].append(self.get_key_of_value(on_mind))

            for ind, ls in  enumerate(to_add_ls):

                if ind < len(to_add_ls) -1:
                    ls.append('0')

        # теперь в списке "to_add_ls" лежат списки одинакового размера, которорые нужно сложить

        # будет содержать строку с результатом
        result_str = ''

        on_mind = 0

        for ind in range(len(to_add_ls[0])):

            n_res = 0

            for ls in to_add_ls:
                n_res += (on_mind + Hex_num.hex_map[ls[ind]])

            on_mind = n_res // 16
            n_res = n_res % 16

            result_str += self.get_key_of_value(n_res)

        if on_mind:
            result_str += self.get_key_of_value(on_mind)

        return Hex_num(result_str[::-1])


num_1_str = input('Введите цифры первого числа (от 0 до F)\n').upper()
num_1 = Hex_num(num_1_str)

num_2_str = input('Введите цифры второго числа (от 0 до F)\n').upper()
num_2 = Hex_num(num_2_str)

if num_1 and num_2:
    num_3 = num_1 + num_2
    print(f'{num_1} + {num_2} = {num_3}')

    num_4 = num_1 * num_2
    print(f'{num_1} * {num_2} = {num_4}')
