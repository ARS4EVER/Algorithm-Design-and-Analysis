def improved_binary_search(arr, target):  
    left, right = 0, len(arr) - 1  
    
    while left <= right:  
        # 计算中间点  
        mid1 = left + (right - left) // 3  
        mid2 = right - (right - left) // 3  

        # 检查中间点  
        if arr[mid1] == target:  
            return mid1  
        if arr[mid2] == target:  
            return mid2  

        if target < arr[mid1]:  
            right = mid1 - 1  
        elif target > arr[mid2]:  
            left = mid2 + 1  
        else:  
            left = mid1 + 1  
            right = mid2 - 1  

    return -1  # 未找到  


# 输入功能  
def main():  
    # 输入数据  
    arr = list(map(int, input("请输入有序数组（用空格分隔）：").split()))  
    target = int(input("请输入要查找的目标值："))  

    # 处理数据  
    index = improved_binary_search(arr, target)  

    # 输出结果  
    if index != -1:  
        print(f"目标值 {target} 在数组中的索引为：{index}")  
    else:  
        print("目标值未找到。")  

# 运行代码  
if __name__ == "__main__":  
    main()  