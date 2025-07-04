n = int(input())
nums = list(map(int,input().split())) #读取输入
def maxSum():
    sum, a, left, right, tempLeft = 0, 0, 0, 0, 0 #初始化变量
    for i in range(0, n):
        a += nums[i] 
        if a < 0: #若当前子列和为负则重置
            a, tempLeft = 0, i + 1  # 更新可能的起始位置为下一个元素
        if a > sum: #找到更大的子列和
            sum,left, right = a, tempLeft, i
    return sum, left, right
sum, left, right = maxSum()
print(f"{sum}")