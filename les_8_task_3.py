'''
Написать программу, которая обходит не взвешенный ориентированный граф без петель,
в котором все вершины связаны, по алгоритму поиска в глубину (Depth-First Search).
'''


def create_graph(n):
    return {j: {i for i in range(n) if i != j} for j in range(n)}


def dfs(graph, start=0, visited=None):

    if visited is None:
        visited = set()

    visited.add(start)

    for next in graph[start] - visited:
        dfs(graph, next, visited)

    return visited


n = int(input('Укажите количество вершин графа\n'))

grahp = create_graph(n)

# список смежности имеет вид:
print('Матрица смежности полученного графа:')
for ind, st in grahp.items():
    print(f'{ind}: {st}')

print('посещенные вершины:', dfs(grahp), sep='\n')
