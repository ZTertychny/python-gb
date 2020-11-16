# 3. Написать программу, которая обходит не взвешенный ориентированный граф без петель, в котором все вершины связаны, по алгоритму поиска в глубину (Depth-First Search).
# Примечания:
# a. граф должен храниться в виде списка смежности;
# b. генерация графа выполняется в отдельной функции, которая принимает на вход число вершин

num_of_vertex = int(input('Введите количество вершин: '))


def generate_graph(number_vertex):
    graph = {}

    for key in range(number_vertex):
        set_edges = set()
        for value in range(number_vertex):
            if value != key:
                set_edges.add(value)
        graph[key] = set_edges
    return graph


def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    if start in visited:
        return visited

    visited.add(start)
    print(f'Для отслеживания правильности работы выводятся посещенные вершины - {visited}')
    for next_edge in graph[start]:
        if next_edge not in visited:
            dfs(graph, next_edge, visited)

    return f'Финальный результат - {visited}'


graph_1 = generate_graph(num_of_vertex)
print(f'Получившийся граф в виде списка смежности: {graph_1}\n')
print(dfs(graph_1, 0))
