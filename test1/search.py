# -*- coding: utf-8 -*- 
# @Time : 2021/3/16 16:07 
# @Author : HGuoo 
# @File : search.py
from test1.cal_time import *


@cal_time
def linear_search(lst, val):
    for i in range(len(lst) - 1):
        if val == lst[i]:
            return val
    return None


@cal_time
def binary_search(lst, val):
    left = 0
    right = len(lst) - 1
    while left <= right:
        mid = (left + right) // 2
        if lst[mid] == val:
            return mid
        elif lst[mid] > val:
            right = mid - 1
        else:
            left = mid + 1

    return None


li = list(range(10000000))
binary_search(li, 4325521)
linear_search(li, 92888)
