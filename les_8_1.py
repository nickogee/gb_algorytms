'''
кратчайший путь
'''

from collections import  deque

g = [
    [0, 1, 1, 0, 1, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0],
    [1, 0, 1, 0, 0, 0, 1, 0],
    [0, 0, 0, 1, 0, 0, 1, 1],
    [0, 0, 0, 0, 1, 1, 0, 1],
    [0, 0, 0, 0, 0, 1, 1, 0],
]


def bfs(graph, start, finish):
    parent = [None for _ in range(len(graph))]
    is_visited = [False for _ in range(len(graph))]

    deq = deque([start])
    is_visited[start] = True

    while len(deq) > 0:

        # извлекаем вершину из конца очереди
        curent = deq.pop()

        # если вершина - искомая, то завершаем цикл
        if curent == finish:
            # return parent
            break

        for i, vertex in enumerate(graph[curent]):
            if vertex == 1 and not is_visited[i]:

                is_visited[i] = True
                parent[i] = curent
                deq.appendleft(i)

    else:
        print(f'Из вершины {start} нельзя попасть в вершину {finish}')

    cost = 0
    way = deque([finish])
    i = finish

    while parent[i] != start:
        cost += 1
        way.appendleft(parent[i])
        i = parent[i]

    cost += 1
    way.appendleft(start)

    print(f'Кратчайший путь {list(way)} длиною в {cost} условных единиц')


s = int(input('начало пути\n'))
f = int(input('конец пути\n'))

bfs(g, s, f)
