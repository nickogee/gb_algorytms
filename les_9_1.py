'''
деревья
'''

from binarytree import tree, bst, Node, build

# класс узел
class MyNode:

    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

# бинарное сбалансированное дерево
a = tree(height=4, is_perfect=False)
print(a)

# бинарное идеальное дерево, поисковое
b = bst(height=3, is_perfect=True)
print(b)

# создание дерева с помощю узлов
c = Node(7)
c.left = Node(3)
c.right = Node(11)
c.left.left = Node(1)
c.left.right = Node(5)
c.right.left = Node(9)
c.right.right = Node(13)
print(c)

d = build([7, 3, 11, 1, 5, 9, 13])
print(d)

e = build([7, 3, 11, 1, 5, 9, 13, None, 2, None, 6])
print(e)

