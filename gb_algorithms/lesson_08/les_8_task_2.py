# 2. Доработать алгоритм Дейкстры (рассматривался на уроке), чтобы он дополнительно возвращал список вершин, которые необходимо обойти.

g = [
    [0, 0, 1, 1, 9, 0, 0, 0],
    [0, 0, 9, 4, 0, 0, 5, 0],
    [0, 9, 0, 0, 3, 0, 6, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 5, 0],
    [0, 0, 7, 0, 8, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 3, 0]
]


def dejkstra(graph, start):
    length = len(graph)
    is_visited = [False] * length
    cost = [float('inf')] * length
    ways = {key: [] for key in range(length)}
    parent = [-1] * length
    parent[start] = start

    cost[start] = 0
    min_cost = 0

    while min_cost < float('inf'):
        is_visited[start] = True

        for i, vertex in enumerate(graph[start]):
            if vertex != 0 and not is_visited[i]:

                if cost[i] > vertex + cost[start]:
                    cost[i] = vertex + cost[start]
                    parent[i] = start

        min_cost = float('inf')
        for i in range(length):
            if min_cost > cost[i] and not is_visited[i]:
                min_cost = cost[i]
                start = i

    for key, value in ways.items():
        for vertex, previous_vertex in enumerate(parent):
            if key == vertex:
                while previous_vertex != parent[previous_vertex]:
                    value.append(previous_vertex)
                    previous_vertex = parent[previous_vertex]
                if previous_vertex >= 0 and previous_vertex == parent[previous_vertex]:
                    value.append(parent[previous_vertex])
                else:
                    value.append('Нет пути')
                value.reverse()
                if value[-1] != vertex and value[-1] != 'Нет пути':
                    value.append(vertex)

    return f'Стоимость до каждой вершины - {cost}\nСписок с вершинами, которые надо пройти - {ways}'


print(dejkstra(g, 0))
