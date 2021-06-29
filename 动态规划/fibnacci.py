# -*- coding: utf-8 -*- 
# @Time : 2021/6/23 16:13 
# @Author : HGuoo 
# @File : fibnacci.py


# F[n] = F[n-1]+F[n-2] F[0]=F[1]=1


# 递归效率低：子问题的重复计算
def fibnacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibnacci(n - 1) + fibnacci(n - 2)


# 动态规划（DP）的思想：递推式， 重复子问题
def fibnacci_no_recurision(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        f = [0, 1, 1]
        for i in range(n - 2):
            num = f[-1] + f[-2]
            f.append(num)
    return f[n]


print(fibnacci_no_recurision(32))
