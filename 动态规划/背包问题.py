# -*- coding: utf-8 -*- 
# @Time : 2021/6/29 15:42 
# @Author : HGuoo 
# @File : 背包问题.py


# 01背包问题
# 将n件商品装入容量为c的最大价值
# 递推式：
# 1.第n件商品体积大于背包容量，不加入背包 f[n][c] = f[n-1][c]
# 2.能装第n件商品，但可以选择装，也可以选择不装，取最大价值的组合 f[n][c] = max(f[n-1][c], f[n-1][c-v[i]]+p[i])
# (value, volume, stock)
goods = [[2, 2, 2], [4, 3, 3], [3, 5, 3], [7, 5, 2]]


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


def backpack_0_1(goods, c):
    n = len(goods)
    dp = [[0 for _ in range(c + 1)] for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, c + 1):
            dp[i][j] = dp[i - 1][j]
            if j >= goods[i - 1][1]:
                dp[i][j] = max(dp[i][j], dp[i - 1][j - goods[i - 1][1]] + goods[i - 1][0])
    return dp[n][c]


# 01背包问题一维优化
# dp[v] = max(dp[v], dp[v-vi]+pi)
# dp[i][v]=max{dp[i-1][v],dp[i-1][v-vi]+pi}
# 一维递推式中的dp[v-vi]+pi替换掉了二维的dp[i-1][v-vi]+pi，所以需要保证dp[v-vi]是第i-1次循环得到的值，而不是第i次循环得到的值，
# 如果内层循环仍然升序遍历的话，那么在当前第i次外层循环求dp[v]的时候，dp[v-vi]一定会是当前第i次外层循环计算得出的，因为v-vi < v，升序
# 遍历会先计算dp[v-vi]，那么这个值代入递推式中计算是错误的。如果内层循环选择降序遍历的话，那么在当前第i次外层循环求dp[v]的时候，dp[v-vi]在
# 在当前第i次外层循环中还未被计算，但在第i-1次外层循环中以及得到了计算，所以此时的dp[v-vi]，dp[v]满足递推式的要求。
def backpack_01_2(goods, c):
    n = len(goods)
    dp = [0 for _ in range(c + 1)]
    for i in range(1, n + 1):
        for j in range(c, 0, -1):
            dp[j] = max(dp[j], dp[j - goods[i - 1][1]] + goods[i - 1][0])
    return dp[-1]


# 完全背包问题
# 有 N 种物品和一个容量是 V 的背包，每种物品都有无限件可用。
# 第 i 种物品的体积是 vi，价值是 wi。
# 求解将哪些物品装入背包，可使这些物品的总体积不超过背包容量，且总价值最大。
# 输出最大价值。
def backpack_complete(goods, c):
    n = len(goods)
    dp = [[0 for _ in range(c + 1)] for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, c + 1):
            for k in range(0, j // goods[i - 1][1] + 1):
                dp[i][j] = max(dp[i][j], dp[i - 1][j - k * goods[i - 1][1]] + k * goods[i - 1][0])
    return dp[-1][-1]


def backpack_complete_2(goods, c):
    n = len(goods)
    dp = [0 for _ in range(c + 1)]
    for i in range(1, n + 1):
        for j in range(c, 0, -1):
            for k in range(0, j // goods[i - 1][1] + 1):
                dp[j] = max(dp[j], dp[j - k * goods[i - 1][1]] + k * goods[i - 1][0])
    return dp[-1]


# dp[i][v] = max(dp[i-1][v] , dp[i][v-vi] + pi)
# 与01背包不同点在于dp[i][v-vi] + pi是i而不是i-1，这表示不取第i件商品的最大价值与取一件第i件商品后，在前i件商品中的最大价值，这意味着可以
# 重复取第i件商品， 所以两者的最大值就是在前i件商品中装入容量v的背包中的最大价值
def backpack_complete_3(goods, c):
    n = len(goods)
    dp = [0 for _ in range(c + 1)]
    for i in range(1, n + 1):
        # 这里是升序，因为需要的是dp[i][v-vi] + pi
        for j in range(goods[i - 1][1], c + 1):
            # max中的dp[j]是第i-1次循环中计算得出的，dp[j-vi]+p[i]是第i次循环计算得出的
            dp[j] = max(dp[j], dp[j - goods[i - 1][1]] + goods[i - 1][0])
    return dp[-1]


print(backpack_complete_3(goods, 19))


# 多重背包问题
# 有 N 种物品和一个容量是 V 的背包。
# 第 i 种物品最多有 si 件，每件体积是 vi，价值是 wi。
# 求解将哪些物品装入背包，可使物品体积总和不超过背包容量，且价值总和最大。
# 输出最大价值。

def backpack_multi(goods, c):
    n = len(goods)
    dp = [0 for _ in range(c + 1)]
    for i in range(1, n + 1):
        for j in range(c, 0, -1):
            kmin = min(j // goods[i - 1][1], goods[i - 1][2])
            for k in range(0, kmin + 1):
                dp[j] = max(dp[j], dp[j - k * goods[i - 1][1]] + k * goods[i - 1][0])

    return dp[-1]
