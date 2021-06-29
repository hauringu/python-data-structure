# -*- coding: utf-8 -*- 
# @Time : 2021/6/23 14:29 
# @Author : HGuoo 
# @File : 拼接最大数字问题.py


# 将一组非负整数按照字符串的方式拼接起来，如何得到最大的数字

from functools import cmp_to_key

li = [32, 94, 88, 944, 9499]


def xy_cmp(x, y):
    if x + y < y + x:
        return 1
    elif x + y > y + x:
        return -1
    else:
        return 0


# 贪心算法
def join_max_number(li):
    li = list(map(str, li))
    # x+y > y+x 则两者交换
    # li.sort(key=cmp_to_key(xy_cmp))
    for i in range(len(li) - 1):
        n = li[i]
        for j in range(i + 1, len(li)):
            if li[j] + n > n + li[j]:
                li[i], li[j] = li[j], li[i]

    return "".join(li)


print(join_max_number(li))
