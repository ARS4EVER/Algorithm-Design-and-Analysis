def karatsuba(x, y):  
    # 将x和y转换为字符串，以便进行分割  
    str_x = str(x)  
    str_y = str(y)  
    
    # 获取两个数字的长度  
    n = max(len(str_x), len(str_y))  
    
    # 如果数字长度小于等于1，直接返回乘积  
    if n == 0:  
        return 0  
    if n == 1:  
        return x * y  
    
    # 计算n的一半，向上取整  
    half = (n + 1) // 2  
    
    # 将x和y拆分为两部分  
    high1 = x // 10**half  # x的高位部分  
    low1 = x % 10**half    # x的低位部分  
    high2 = y // 10**half  # y的高位部分  
    low2 = y % 10**half    # y的低位部分  
    
    # 递归调用 Karatsuba 计算高位和低位的乘积  
    z0 = karatsuba(low1, low2)          # low1 * low2  
    z1 = karatsuba((low1 + high1), (low2 + high2))  # (low1 + high1) * (low2 + high2)  
    z2 = karatsuba(high1, high2)        # high1 * high2  

    # 根据Karatsuba公式组合结果  
    result = z2 * 10**(2 * half) + (z1 - z2 - z0) * 10**half + z0  
    return result  

# 示例使用  
if __name__ == "__main__":  
    # 用户输入大整数  
    num1 = int(input("请输入第一个大整数: "))  
    num2 = int(input("请输入第二个大整数: "))  
    product = karatsuba(num1, num2)  
    print(f"{num1} * {num2} = {product}")  