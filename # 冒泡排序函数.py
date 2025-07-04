# 冒泡排序函数
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):  # 标记是否发生交换
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # 交换相邻元素
                swapped = True
        if not swapped:         # 如果没有发生交换，说明数组已经有序，提前退出1
            break

# 主函数：数据输入、处理和输出
def main():
    input_data = input("请输入要排序的数字，用空格分隔: ")
    arr = list(map(int, input_data.split())) 
    bubble_sort(arr)
    print("冒泡排序结果:", arr)

# 运行主程序
if __name__ == "__main__":
    main()