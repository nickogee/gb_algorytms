'''
Закодируйте любую строку по алгоритму Хаффмана.
'''

from collections import OrderedDict


# класс узел
class MyNode:

    def __init__(self, data, freq, left=None, right=None):
        self.data = data
        self.freq = freq
        self.left = left
        self.right = right


def Huffman_encode(s):

    def encode(root, st, huffman_code):
        if root is None:
            return

        # обнаружили листовой узел
        if not root.left and not root.right:
            huffman_code[root.data] = st if len(st) > 0 else '1'

        encode(root.left, st + '0', huffman_code)
        encode(root.right, st + '1', huffman_code)

    # подсчитываем частоту появления каждого символаб создадим листовые уровни для символов
    # и сохраним его в словаре {Node: freq}
    # freq = {i: s.count(i) for i in set(s)}
    freq = {MyNode(k, s.count(k)): s.count(k) for k in set(s)}

    # данные словаря упорядочим по частоте в упорядоченном словаре
    # pq = [MyNode(k, v) for k, v in freq.items()]
    ord_freq = OrderedDict(sorted(freq.items(), key=lambda x: x[1]))

    # пока в словаре не останется один узел - корень
    while len(ord_freq) != 1:

        # Удалиv два узла с наивысшим приоритетом
        # (самая низкая частота) из ord_freq
        left = ord_freq.popitem(last=False)[0]
        right = ord_freq.popitem(last=False)[0]

        # создадим новый внутренний узел с этими двумя узлами в качестве дочерних и
        # с частотой, равной сумме частот двух узлов.
        # Добавим новый узел в приоритетную очередь.
        total = left.freq + right.freq
        ord_freq[MyNode(None, total, left, right)] = total

        # снова отсортеруем упорядоченный словарь, т.к. добавиил новый эл-т
        ord_freq = OrderedDict(sorted(ord_freq.items(), key=lambda x: x[1]))

    # теперь здесь у нас корень дерева
    root = ord_freq.popitem()[0]

    # проходим по дереву Хаффмана и сохраняем коды Хаффмана в словаре.
    huffmanCode = {}
    encode(root, '', huffmanCode)

    print(f'Строка {s} закодирована алгоритмом Хафмана:\n{huffmanCode}')


s_1 = input('Введите строку\n')

Huffman_encode(s_1)
