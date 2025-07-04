import time

def knapsack_backtrack(weights, values, capacity):
    n = len(weights)  # 物品数量
    max_value = [0]  # 最大价值
    best_solution = [0] * n  # 最优解方案

    def backtrack(i, current_weight, current_value, solution):
        if i == n:  # 所有物品已处理
            if current_value > max_value[0]:  # 更新最大价值和最优解
                max_value[0] = current_value
                best_solution[:] = solution[:]
            return
        solution[i] = 0  # 不选第 i 个物品
        backtrack(i + 1, current_weight, current_value, solution)
        if current_weight + weights[i] <= capacity:  # 选第 i 个物品
            solution[i] = 1
            backtrack(i + 1, current_weight + weights[i], current_value + values[i], solution)
            solution[i] = 0  # 回溯

    solution = [0] * n  # 初始化解
    backtrack(0, 0, 0, solution)  # 开始回溯
    return max_value[0], best_solution

#限制上下界

# 数据输入
def input_data():
    n = int(input("请输入物品数量: "))  # 输入物品数量
    weights = list(map(int, input("请输入每个物品的重量（空格分隔）: ").split()))  # 输入重量
    values = list(map(int, input("请输入每个物品的价值（空格分隔）: ").split()))  # 输入价值
    capacity = int(input("请输入背包容量: "))  # 输入背包容量
    return weights, values, capacity

# 数据输出
def output_result(max_value, best_solution):
    print(f"最大价值: {max_value}")  # 输出最大价值
    print(f"选择的物品: {best_solution}")  # 输出选择方案

if __name__ == "__main__":
    weights, values, capacity = input_data()  # 获取输入
    max_value, best_solution = knapsack_backtrack(weights, values, capacity)  # 求解
    output_result(max_value, best_solution)  # 输出结果