"""
main.py
Script principal que:
- lê os dados fictícios em data/entregas.csv
- constrói um grafo simples (fictício) com pesos (distância euclidiana)
- executa A* entre um par de pontos de exemplo
- executa K-Means para agrupar entregas
- salva outputs em /outputs
Comentários didáticos incluídos.
"""

import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import os
import math
from src.a_star import a_star
from src.kmeans import agrupar_entregas

# ------- Carregar dados -------
data_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'entregas.csv')
df = pd.read_csv(data_path)

# ------- Construir posições (dicionário) -------
positions = {row['nome']: (row['x'], row['y']) for _, row in df.iterrows()}

# ------- Construir grafo simples -------
# Para fins didáticos, conectamos cada ponto ao seu 3 vizinhos mais próximos (por distância euclidiana)
graph = {}
for name, pos in positions.items():
    # calcular distâncias para todos os outros pontos
    dists = []
    for other, opos in positions.items():
        if other == name:
            continue
        dx = pos[0] - opos[0]
        dy = pos[1] - opos[1]
        d = math.hypot(dx, dy)
        dists.append((other, d))
    # ordenar e pegar 3 mais próximos
    dists.sort(key=lambda x: x[1])
    neighbors = {n: round(dist,2) for n, dist in dists[:3]}  # pesos arredondados
    graph[name] = neighbors

# ------- Salvar imagem do grafo -------
G = nx.Graph()
for n, neighs in graph.items():
    for m, w in neighs.items():
        G.add_edge(n, m, weight=w)
os.makedirs(os.path.join(os.path.dirname(__file__), '..', 'outputs'), exist_ok=True)
pos_nx = {n: positions[n] for n in positions}
plt.figure(figsize=(6,6))
nx.draw(G, pos_nx, with_labels=True, node_color='lightblue')
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos_nx, edge_labels=labels)
plt.title("Grafo de Pontos de Entrega (fictício)")
plt.savefig(os.path.join(os.path.dirname(__file__), '..', 'outputs', 'grafo.png'))
plt.close()

# ------- Executar A* (exemplo: Ponto_A -> Ponto_F) -------
start = 'Ponto_A'
goal = 'Ponto_F'
path, cost = a_star(graph, positions, start, goal)

with open(os.path.join(os.path.dirname(__file__), '..', 'outputs', 'rota_exemplo.txt'), 'w') as f:
    if path is None:
        f.write("Rota não encontrada entre {} e {}".format(start, goal))
    else:
        f.write("Rota: " + " -> ".join(path) + "\n")
        f.write("Custo total (soma de pesos): {:.2f}\n".format(cost))

# ------- Executar K-Means (exemplo k=2) -------
k = 2
clusters_df = agrupar_entregas(df[['id','nome','x','y']].rename(columns={'nome':'nome'}).set_index('id').reset_index(drop=False), k=k, save_path=os.path.join(os.path.dirname(__file__), '..', 'outputs', 'clusters.png'))

# ------- Salvar CSV com clusters -------
clusters_df.to_csv(os.path.join(os.path.dirname(__file__), '..', 'outputs', 'entregas_com_clusters.csv'), index=False)

print("Execução concluída. Verifique a pasta outputs/ para grafo.png, clusters.png, rota_exemplo.txt e entregas_com_clusters.csv")
