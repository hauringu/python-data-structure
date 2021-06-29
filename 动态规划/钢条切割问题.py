# -*- coding: utf-8 -*- 
# @Time : 2021/6/23 16:45 
# @Author : HGuoo 
# @File : 钢条切割问题.py


# 钢条切割问题--最优子结构
# 最优子结构：可以将规模为n的问题分解为更小规模的问题，子问题的最优解可以组合成原问题的最优解，也就是说可以找到递推式


def cut_steel(n):
    # 长度为i的最大分割价格为f[i]
    f = [0, 1, 5, 8, 10, 13, 17, 18, 22, 25, 30]
    for i in range(n - 10):
        max = f[1] + f[(i + 11) - 1]
        for j in range(1, (i + 11) // 2 + 1):
            if max < f[j] + f[(i + 11) - j]:
                max = f[j] + f[(i + 11) - j]
        f.append(max)
    return f[n]


# 长度为i的价格为p[i]
p = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]


def cut_steel_recurision_1(p, n):
    res = 0
    if n < len(p):
        res = p[n]
    for i in range(1, n // 2 + 1):
        res = max(res, cut_steel_recurision_1(p, i) + cut_steel_recurision_1(p, n - i))
    return res


# 左边不切割，右边切割
def cut_steel_recurision_2(p, n):
    if n >= len(p):
        raise IndexError
    res = p[n]
    for i in range(1, n//2+1):
        res = max(res, p[i] + cut_steel_recurision_2(p, n - i))
    return res


def cut_steel_dp(p, n):
    # 保存最优切割方案的价值
    r = [0]
    # 保存最优切割方案左边不切割的长度
    s = [0]
    for i in range(1, n+1):
        res = p[i]
        l = i
        for j in range(1, i//2+1):
            if res < p[j] + r[i-j]:
                l = j
        s.append(l)
        r.append(res)
    scheme = []
    k = n
    while k > 0:
        scheme.append(s[k])
        k -= s[k]
    return r[n], scheme



print(cut_steel(20))
print(cut_steel_recurision_1(p, 15))
print(cut_steel_recurision_2(p, 9))
print(cut_steel_dp(p, 6))
