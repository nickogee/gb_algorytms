'''
Алгоритм Дейкстры
'''



g = [
    [0, 0, 1, 1, 9, 0, 0, 0],
    [0, 0, 9, 4, 0, 0, 5, 0],
    [0, 9, 0, 0, 3, 0, 6, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 5, 0],
    [0, 0, 7, 0, 8, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 2, 0],
]


def dykstr(graph, start):
    leght = len(graph)
    is_visited = [False] * leght
    coast = [float('inf')] * leght
    parent = [-1] * leght

    # стоимость пути до начальной вершины = 0 (мы уже в ней находимся)
    coast[start] = 0
    min_coast = 0

    while min_coast < float('inf'):

        is_visited[start] = True

        for i, vertex in enumerate(graph[start]):
            if vertex != 0 and not is_visited[i]:

                if coast[i] > vertex + coast[start]:
                    coast[i] = vertex + coast[start]
                    parent[i] = start

        min_coast = float('inf')
        for i in range(leght):
            if min_coast > coast[i] and not is_visited[i]:
                min_coast = coast[i]
                start = i

    return coast


s = int(input('начало пути\n'))
print(dykstr(g, s))





