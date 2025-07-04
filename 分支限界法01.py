class Item:
    def __init__(self, value, weight):
        # 初始化物品类，包含价值、重量和价值重量比
        self.value = value
        self.weight = weight
        self.ratio = value / weight

def knapsack_branch_and_bound(items, capacity):
    # 按照价值重量比从大到小排序物品
    items.sort(key=lambda x: x.ratio, reverse=True)

    # 初始化最大价值和最佳解
    max_value = 0
    best_solution = [0] * len(items)

    def bound(node_index, current_value, current_weight):
        # 计算当前节点的上界
        if current_weight >= capacity:
            return 0
        bound_value = current_value
        remaining_capacity = capacity - current_weight
        for i in range(node_index, len(items)):
            if items[i].weight <= remaining_capacity:
                bound_value += items[i].value
                remaining_capacity -= items[i].weight
            else:
                bound_value += items[i].ratio * remaining_capacity
                break
        return bound_value

    def branch_and_bound(node_index, current_value, current_weight, solution):
        nonlocal max_value, best_solution

        # 如果当前重量超过背包容量，直接返回
        if current_weight > capacity:
            return

        # 更新最大价值和最佳解
        if current_value > max_value:
            max_value = current_value
            best_solution = solution[:]

        # 如果所有物品都已考虑，直接返回
        if node_index >= len(items):
            return

        # 计算当前节点的上界
        upper_bound = bound(node_index, current_value, current_weight)
        if upper_bound <= max_value:
            return

        # 分支：选择当前物品
        solution[node_index] = 1
        branch_and_bound(node_index + 1, current_value + items[node_index].value, current_weight + items[node_index].weight, solution)

        # 分支：不选择当前物品
        solution[node_index] = 0
        branch_and_bound(node_index + 1, current_value, current_weight, solution)

    # 开始分支限界法
    branch_and_bound(0, 0, 0, [0] * len(items))

    return max_value, best_solution

# 输入数据
def input_data():
    n = int(input("请输入物品数量: "))
    capacity = int(input("请输入背包容量: "))
    weights = list(map(int, input("请输入每个物品的重量（空格分隔）: ").split()))
    values = list(map(int, input("请输入每个物品的价值（空格分隔）: ").split()))
    items = [Item(values[i], weights[i]) for i in range(n)]
    return items, capacity

# 输出结果
def output_results(max_value, solution, items):
    print(f"最大价值: {max_value}")
    print(f"选择的物品: {solution}")

# 主函数
def main():
    items, capacity = input_data()
    max_value, solution = knapsack_branch_and_bound(items, capacity)
    output_results(max_value, solution, items)

if __name__ == "__main__":
    main()