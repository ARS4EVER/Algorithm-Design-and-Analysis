import sys
from collections import defaultdict

class Graph:
    def __init__(self):
        self.edges = defaultdict(dict)
    
    def add_edge(self, u, v, weight):
        self.edges[u][v] = weight
    
    def min_cost_path(self, start, end):
        # 初始化cost和path字典
        cost = {node: float('inf') for node in self.edges}
        cost[end] = 0
        path = {}
        
        # 手动定义多段图的阶段顺序
        stages = [['S'], ['A', 'B'], ['C'], ['T']]
        
        # 动态规划处理，从后向前计算
        for i in range(len(stages)-2, -1, -1):
            for node in stages[i]:
                # 遍历所有后继节点
                for neighbor in self.edges[node]:
                    if cost[node] > self.edges[node][neighbor] + cost[neighbor]:
                        cost[node] = self.edges[node][neighbor] + cost[neighbor]
                        path[node] = neighbor
        
        # 重建路径
        if start not in path:
            return float('inf'), []
        
        current = start
        min_path = [current]
        while current != end:
            current = path[current]
            min_path.append(current)
        
        return cost[start], min_path

# 创建图并添加边
g = Graph()
g.add_edge('S', 'A', 1)
g.add_edge('S', 'B', 4)
g.add_edge('A', 'C', 1)
g.add_edge('B', 'C', 2)
g.add_edge('C', 'T', 1)
g.add_edge('A', 'T', 6)
g.add_edge('B', 'T', 3)

# 计算最小成本路径
min_cost, path = g.min_cost_path('S', 'T')

# 按照要求格式输出结果
print("所有路径中最短路径：", path)
print("最小总代价：", min_cost)