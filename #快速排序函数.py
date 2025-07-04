#快速排序函数
def quick_sort(arr):
    if len(arr)<=1:
        return arr #数组长度为1或0直接输出
    pivot=arr[0] #选择基准元素
    less_than_pivot=[x for x in arr[1:] if x<=pivot]#使用分治思想将数组分为大于基准和小于基准两部分
    biggeer_than_pivot=[x for x in arr[1:] if x>pivot]
    return quick_sort(less_than_pivot)+[pivot]+quick_sort( biggeer_than_pivot)#递归调用合并结果

#主函数
def main():
    input_data=input("输入数字，用空格隔开：")
    arr=list(map(int,input_data.split()))
    sorted_arr=quick_sort(arr)
    print("排序结果:",sorted_arr)

#运行主程序
if __name__=="__main__":
    main()

    