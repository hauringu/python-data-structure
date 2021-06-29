# -*- coding: utf-8 -*- 
# @Time : 2021/6/22 16:11 
# @Author : HGuoo 
# @File : 找零问题.py


# 找零n元， 100、50、20、10、5、1，怎么使钱的张数最少

t = [100, 50, 20, 10, 5, 1]


def change(t, n):
    m = [0 for _ in range(len(t))]
    for i, money in enumerate(t):
        m[i] = n // money
        n = n % money
        print("%d张%d元" % (m[i], money))


change(t, 165)
