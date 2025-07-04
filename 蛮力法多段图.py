class Graph:
    def __init__(self):
        self.adj = {}  # 使用字典存储邻接表，key为顶点，value为邻居节点和边的权重

    def add_vertex(self, v):
        # 添加新顶点，如果不存在就创建一个空的邻居列表
        if v not in self.adj:
            self.adj[v] = []

    def add_edge(self, u, v, weight):
        # 添加一条有向边u -> v，参数为边的权重
        if u not in self.adj:
            self.add_vertex(u)
        if v not in self.adj:
            self.add_vertex(v)
        self.adj[u].append((v, weight))  # 在u的邻居列表中加入(v, weight)

def all_paths(graph, start, end, path, all_paths_list, current_weight):
    # 递归搜索所有从start到end的路径
    path.append(start)  # 将当前节点加入路径中
    if start == end:
        # 当到达终点时，将当前路径及其总成本加入结果列表
        all_paths_list.append((list(path), current_weight))
    else:
        # 遍历所有邻居，递归搜索路径
        for (neighbor, weight) in graph.adj[start]:
            if neighbor not in path:  # 避免环路
                # 递归调用，路径更新
                all_paths(graph, neighbor, end, path, all_paths_list, current_weight + weight)
    # 退回上一步，尝试其他路径
    path.pop()

# 创建图对象
g = Graph()
# 添加边，定义图的结构
g.add_edge('S', 'A', 1)
g.add_edge('S', 'B', 4)
g.add_edge('A', 'C', 1)
g.add_edge('B', 'C', 2)
g.add_edge('C', 'T', 1)
g.add_edge('A', 'T', 6)
g.add_edge('B', 'T', 3)

# 存储所有路径的列表
all_paths_list = []

# 调用函数，找出所有从'S'到'T'的路径
all_paths(g, 'S', 'T', [], all_paths_list, 0)

# 如果存在路径，找出成本最小的那条
if all_paths_list:
    min_path, min_cost = min(all_paths_list, key=lambda x: x[1])  # 按照路径成本排序
    print("所有路径中最短路径：", min_path)
    print("最小总代价：", min_cost)
else:
    print("无路径")