"""
a_star.py
Implementação didática e simples do algoritmo A* para grafos representados como dicionário de adjacência.
Os comentários explicam cada passo — ideal para entrega acadêmica.
"""

import heapq
import math

def heuristic(a_pos, b_pos):
    """Heurística: distância euclidiana entre posições (tuplas x,y)."""
    (x1, y1) = a_pos
    (x2, y2) = b_pos
    return math.hypot(x2 - x1, y2 - y1)

def a_star(graph, positions, start, goal):
    """
    graph: dict onde graph[node] = dict(neighbor: weight)
    positions: dict com posições (x,y) de cada nó, usado pela heurística
    start, goal: nós (strings)
    Retorna: (caminho_lista, custo_total) ou (None, None) se não encontrar
    """
    # fila de prioridade: (f_score, g_score, node, path)
    open_heap = []
    heapq.heappush(open_heap, (0 + heuristic(positions[start], positions[goal]), 0, start, [start]))
    # melhor g_score conhecida
    g_scores = {start: 0}
    visited = set()

    while open_heap:
        f, g, current, path = heapq.heappop(open_heap)

        if current == goal:
            return path, g

        if current in visited:
            continue
        visited.add(current)

        for neighbor, weight in graph.get(current, {}).items():
            tentative_g = g + weight
            if neighbor not in g_scores or tentative_g < g_scores[neighbor]:
                g_scores[neighbor] = tentative_g
                f_score = tentative_g + heuristic(positions[neighbor], positions[goal])
                heapq.heappush(open_heap, (f_score, tentative_g, neighbor, path + [neighbor]))

    return None, None
