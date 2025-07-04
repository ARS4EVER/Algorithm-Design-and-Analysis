def recursive_binary_search(arr, target, left, right):  
    if left > right:  # 基本情况：如果左指针超过右指针，表示未找到目标  
        return -1  
    
    mid = left + (right - left) // 2  # 计算当前部分的中间索引  
    if arr[mid] == target:  # 比较中间元素与目标  
        return mid  # 找到目标元素，返回索引  
    elif arr[mid] > target:  # 如果中间元素大于目标，继续在左半部分查找  
        return recursive_binary_search(arr, target, left, mid - 1)  
    else:  # 否则在右半部分查找  
        return recursive_binary_search(arr, target, mid + 1, right)  

def main_recursive():  
    arr = list(map(int, input("请输入一个已排序的整数数组（用空格分隔）: ").split()))  
    target = int(input("请输入要查找的目标整数: "))  
    
    result = recursive_binary_search(arr, target, 0, len(arr) - 1)  

    if result != -1:  
        print(f"目标元素 {target} 在数组中的索引是: {result}")  
    else:  
        print(f"目标元素 {target} 未在数组中找到。")  

if __name__ == "__main__":  
    main_recursive()  