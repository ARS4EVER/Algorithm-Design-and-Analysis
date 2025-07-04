import heapq 

def prim(graph):

    # 获取图中所有节点
    nodes = list(graph.keys())
    
    # 初始化最小生成树的边列表
    mst = []
    
    # 初始化已访问节点集合，选择第一个节点作为起点
    visited = set([nodes[0]])
    
    # 初始化边的优先队列，将起点的所有边加入队列
    edges = [
        (cost, nodes[0], neighbor)  # 每条边用三元组 (权重, 起点, 终点) 表示
        for neighbor, cost in graph[nodes[0]].items()
    ]
    heapq.heapify(edges)  # 将边列表转化为最小堆
    
    # 当优先队列中还有边时，继续循环
    while edges:
        # 弹出权重最小的边
        cost, u, v = heapq.heappop(edges)
        
        # 如果终点节点尚未访问，则将其加入最小生成树
        if v not in visited:
            visited.add(v)  # 标记终点节点为已访问
            mst.append((u, v, cost))  # 将边加入最小生成树
            
            # 将终点节点的所有未访问邻居的边加入优先队列
            for neighbor, cost in graph[v].items():
                if neighbor not in visited:
                    heapq.heappush(edges, (cost, v, neighbor))
    
    return mst  

graph = {
    'A': {'B': 2, 'D': 6},  
    'B': {'A': 2, 'C': 3, 'D': 8}, 
    'C': {'B': 3, 'D': 4},  
    'D': {'A': 6, 'B': 8, 'C': 4}  
}

mst_prim = prim(graph)
print("Prim算法生成的最小生成树：", mst_prim) 