'''
На улице встретились N друзей. Каждый пожал руку всем остальным друзьям (по одному разу). Сколько рукопожатий было?
'''

from collections import deque

n = int(input('Сколько дружей встретились на улице?\n'))

# для этой задачи вершины графа - это каждый из друзей, ребра графа - рукопожатия
# в таком случае каждый элемент графа будет иметь связь с каждым, то есть в матрице смежности нули будут только по
# главной диагонали

g = [[0 if i == j else 1 for i in range(n)] for j in range(n)]

# матрица смежности имеет вид:
print('Матрица смежности полученного графа:')
for st in g:
    print(st)


def handclasp_count(graph):
    leght = len(graph)
    deq = deque([0])

    # счетчик уникальных рукопожатий
    count = 0

    # счетчик друзей
    curent_frend = 0

    while len(deq) > 0:

        # будем учитывать, что каждый последующий друг уже здоровался с предшествующим
        is_clasp = [False if i > curent_frend else True for i in range(leght)]

        # извлекаем вершину из конца очереди
        curent = deq.pop()

        for i, vertex in enumerate(graph[curent]):
            if vertex == 1 and not is_clasp[i]:

                count += 1
                is_clasp[i] = True
                deq.appendleft(i)

        curent_frend += 1

    print(f'Количество уникальных рукопожатий - {count}')
    return


handclasp_count(g)
