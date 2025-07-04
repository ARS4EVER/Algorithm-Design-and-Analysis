class UnionFind:
    def __init__(self, nodes):
        self.parent = {node: node for node in nodes}
    
    def find(self, u):
        while self.parent[u] != u:
            self.parent[u] = self.parent[self.parent[u]]
            u = self.parent[u]
        return u
    
    def union(self, u, v):
        pu, pv = self.find(u), self.find(v)
        if pu != pv:
            self.parent[pv] = pu

def kruskal(graph):
    edges = []
    for u in graph:
        for v, cost in graph[u].items():
            edges.append((cost, u, v))
    edges.sort()  # 按权值排序
    
    nodes = list(graph.keys())
    uf = UnionFind(nodes)
    mst = []
    
    for cost, u, v in edges:
        if uf.find(u) != uf.find(v):
            uf.union(u, v)
            mst.append((u, v, cost))
    return mst
graph = {
    'A': {'B': 2, 'D': 6},
    'B': {'A': 2, 'C': 3, 'D': 8},
    'C': {'B': 3, 'D': 4},
    'D': {'A': 6, 'B': 8, 'C': 4}
}

mst_kruskal = kruskal(graph)
print("Kruskal算法生成的最小生成树：", mst_kruskal)