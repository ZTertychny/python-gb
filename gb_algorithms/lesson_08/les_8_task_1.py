# 1. На улице встретились N друзей. Каждый пожал руку всем остальным друзьям (по одному разу). Сколько рукопожатий было?
#    Примечание. Решите задачу при помощи построения графа.

n_friends = int(input('Сколько друзей встретилось: '))


def handshakes_of_friends(number):
    graph_matrix = []
    ribs = 0

    vertex = 0
    while vertex != number:
        line_matrix = []
        line_matrix = [1 if i > vertex else 0 for i in range(number)]
        graph_matrix.append(line_matrix)

        vertex += 1

    for line in graph_matrix:
        for el in line:
            if el == 1:
                ribs += 1
    return f'Количество рукопожатий {number} друзей составило {ribs}'


print(handshakes_of_friends(n_friends))
