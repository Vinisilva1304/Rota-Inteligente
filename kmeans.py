"""
kmeans.py
Funções para agrupar entregas usando K-Means e plotar clusters.
Comentários didáticos incluídos.
"""
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import os

def agrupar_entregas(df, k=2, save_path="outputs/clusters.png"):
    """
    df: DataFrame com colunas 'x' e 'y'
    k: número de clusters desejado
    Salva um gráfico em save_path e retorna o DataFrame com coluna 'cluster'
    """
    coords = df[['x', 'y']].values
    modelo = KMeans(n_clusters=k, random_state=42)
    clusters = modelo.fit_predict(coords)
    df = df.copy()
    df['cluster'] = clusters

    # Plot simples dos clusters (matplotlib sem especificar cores)
    plt.figure(figsize=(6,5))
    plt.scatter(df['x'], df['y'], c=df['cluster'])
    # marcar centros
    centers = modelo.cluster_centers_
    plt.scatter(centers[:,0], centers[:,1], marker='x', s=100)
    plt.title(f"Clusters de Entregas (K={k})")
    plt.xlabel("x")
    plt.ylabel("y")
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    plt.savefig(save_path)
    plt.close()
    return df
