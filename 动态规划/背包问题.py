# -*- coding: utf-8 -*- 
# @Time : 2021/6/29 15:42 
# @Author : HGuoo 
# @File : 背包问题.py


# 01背包问题
# 将n件商品装入容量为c的最大价值
# 递推式：
# 1.第n件商品体积大于背包容量，不加入背包 f[n][c] = f[n-1][c]
# 2.能装第n件商品，但可以选择装，也可以选择不装，取最大价值的组合 f[n][c] = max(f[n-1][c], f[n-1][c-v[i]]+p[i])
# (value, volume)
goods = [[2, 2], [4, 3], [3, 5], [7, 5]]


def backpack_0_1_recurison(n, c):
    if n == 0 or c == 0:
        return 0
    # 第n件商品体积大于背包容量，不加入背包
    if goods[n - 1][1] > c:
        return backpack_0_1_recurison(n - 1, c)
    # 能装第n件商品，但可以选择装，也可以选择不装，取最大价值的组合
    else:
        return max(backpack_0_1_recurison(n - 1, c),
                   backpack_0_1_recurison(n - 1, c - goods[n - 1][1]) + goods[n - 1][0])


# def backpack_0_1(n,c):

print(backpack_0_1_recurison(4, 10))
