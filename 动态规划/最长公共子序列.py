# -*- coding: utf-8 -*- 
# @Time : 2021/6/28 16:10 
# @Author : HGuoo 
# @File : 最长公共子序列.py

# 一个序列的子序列指从该序列中删除若干元素后得到的序列，可以不连续，但顺序需一致
# 例ABCD, ADF 都是ABCDEF的子序列
# 最长公共子序列（LCS）应用场景：字符串相似度比对


def lcs_recurision(x, y):
    if len(x) == 0 or len(y) == 0:
        return 0
    if x[-1] == y[-1]:
        return lcs_recurision(x[0:-1], y[0:-1]) + 1
    else:
        return max(lcs_recurision(x[0:-1], y), lcs_recurision(x, y[0:-1]))


x = "ABCDBAB"
y = "BDCABA"
print(lcs_recurision(x, y))


def lcs_no_recurision(x, y):
    lcs = [[0 for _ in range(len(y) + 1)] for _ in range(len(x) + 1)]
    for i in range(1, len(x) + 1):
        for j in range(1, len(y) + 1):
            if x[i - 1] == y[j - 1]:
                lcs[i][j] = lcs[i - 1][j - 1] + 1
            else:
                lcs[i][j] = max(lcs[i - 1][j], lcs[i][j - 1])
    return lcs[len(x)][len(y)]


def lcs(x, y):
    m = len(x)
    n = len(y)
    c = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    # 记录匹配字符的方向 1-左上方，意味着匹配 2-上方 3-左方
    b = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if x[i - 1] == y[j - 1]:
                c[i][j] = c[i - 1][j - 1] + 1
                b[i][j] = 1
            elif c[i - 1][j] > c[i][j - 1]:
                c[i][j] = c[i - 1][j]
                b[i][j] = 2
            else:
                c[i][j] = c[i][j - 1]
                b[i][j] = 3
    return c[m][n], b


def lcs_trackback(x, y):
    c, b = lcs(x, y)
    m = len(x)
    n = len(y)
    res = []
    while m > 0 and n > 0:
        if b[m][n] == 1:
            res.append(x[m-1])
            m -= 1
            n -= 1
        elif b[m][n] == 2:
            m -= 1
        else:
            n -= 1
    return "".join(reversed(res))


print(lcs_trackback(x, y))
