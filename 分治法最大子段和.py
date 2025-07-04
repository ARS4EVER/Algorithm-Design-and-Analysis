n = int(input())
nums = list(map(int,input().split()))#读取输入

def maxSum(left,right):
    if left == right:
        return (nums[left] if nums[left] > 0 else 0, left, left)
    else:
        center = (left + right) // 2
        leftSum, leftStart, leftEnd = maxSum(left, center)
        rightSum, rightStart, rightEnd = maxSum(center + 1, right)
 
        s1, lefts, maxLeft = 0, 0, center #从中点向左扫描，计算最大左半部分和
        for i in range(center, left - 1, -1):
            lefts += nums[i]
            if lefts > s1:
                s1, maxLeft = lefts, i
 
        s2, rights, maxRight = 0, 0, center + 1  #从中点向右扫描，计算最大右半部分和
        for i in range(center + 1, right + 1):
            rights += nums[i]
            if rights > s2:
                s2, maxRight = rights, i
 
        sum = s1 + s2  #跨越中点的最大子段和

        if sum >= leftSum and sum >= rightSum:
            return sum, maxLeft, maxRight
        elif leftSum < rightSum:
            return rightSum, rightStart, rightEnd
        else:
            return leftSum, leftStart, leftEnd  #比较三个子段和，返回最大的
sum, left, right = maxSum(0, n-1)
print(f"{sum}")