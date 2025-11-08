# Rota Inteligente: Otimização de Entregas com Algoritmos de IA

## 1. Título
Rota Inteligente: Otimização de Entregas com Algoritmos de IA

## 2. Descrição do Problema
A empresa fictícia **Sabor Express** enfrenta dificuldades para otimizar rotas de entrega de alimentos em horários de pico. Os percursos são definidos manualmente, resultando em atrasos, alto consumo de combustível e insatisfação de clientes.

Este projeto propõe o uso de métodos clássicos de Inteligência Artificial para calcular rotas eficientes e agrupar entregas próximas, reduzindo custos e tempo de deslocamento.

## 3. Objetivo
- Implementar um algoritmo de busca para encontrar o menor caminho entre pontos (A*).
- Agrupar pedidos próximos usando K-Means para formar zonas de entrega.
- Disponibilizar código executável, dados de exemplo e outputs para avaliação.

## 4. Abordagem Adotada
1. Representação do mapa como um **grafo** (nós = pontos fictícios; arestas = ruas com peso = distância).
2. Implementação do **A*** para rotas entre dois nós.
3. Aplicação de **K-Means** sobre coordenadas geográficas fictícias dos pedidos para agrupar entregas em zonas.
4. Geração de plots e avaliações simples (distância total da rota, tamanho dos clusters).

## 5. Algoritmos Utilizados
- **A\*** (A-star) — busca heurística (aqui heurística simples: distância euclidiana entre nós).
- **K-Means** — agrupamento não supervisionado para zonas de entrega.
- **Dijkstra** (mencionado) — pode ser adicionado para comparação.

## 6. Diagrama do Grafo
O repositório contém scripts que geram imagens do grafo (`outputs/grafo.png`) e dos clusters (`outputs/clusters.png`).

## 7. Como executar (passo a passo)
1. Clone o repositório:
```bash
git clone <seu-repo> && cd Rota-Inteligente
```
2. Crie e ative um ambiente virtual (opcional, mas recomendado):
```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate    # Windows (PowerShell)
```
3. Instale dependências:
```bash
pip install -r requirements.txt
```
4. Execute o script principal:
```bash
python src/main.py
```
5. Verifique a pasta `outputs/` para as imagens geradas (grafo, clusters) e prints de rotas.

## 8. Estrutura do repositório
```
Rota-Inteligente/
│
├── README.md
├── requirements.txt
├── /src
│   ├── main.py
│   ├── a_star.py
│   └── kmeans.py
│
├── /data
│   └── entregas.csv
│
├── /outputs
│   ├── grafo.png
│   └── clusters.png
```

## 9. Resultados e análise (exemplo)
- O A* retorna rotas plausíveis entre pontos fictícios.
- K-Means agrupa entregas próximas de modo que cada entregador possa assumir um cluster.
- Limitações: dados sintéticos; sem tráfego em tempo real; heurística simples.

## 10. Melhorias futuras
- Integrar APIs de mapas (Google Maps, OpenStreetMap) para distâncias reais.
- Considerar restrições: janelas de tempo, capacidade dos entregadores.
- Experimentar otimização combinatória (MILP) ou heurísticas meta-heurísticas (genéticos, simulated annealing).

---

Projeto entregue por: Vinícius Silva (Aluno)
Disciplina: Artificial Intelligence Fundamentals
