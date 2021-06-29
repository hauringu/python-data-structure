# -*- coding: utf-8 -*- 
# @Time : 2021/4/6 16:34 
# @Author : HGuoo 
# @File : merge_sort.py
from test1.cal_time import *
import random


def merge(lst, left, mid, right):
    i = left
    j = mid + 1
    l = []
    while i <= mid and j <= right:
        if lst[i] <= lst[j]:
            l.append(lst[i])
            i += 1
        else:
            l.append(lst[j])
            j += 1
    while i <= mid:
        l.append(lst[i])
        i += 1
    while j <= right:
        l.append(lst[j])
        j += 1
    lst[left: right + 1] = l


def _merge_sort(lst, left, right):
    if left < right:
        mid = (left + right) // 2
        _merge_sort(lst, left, mid)
        _merge_sort(lst, mid + 1, right)
        merge(lst, left, mid, right)


@cal_time
def merge_sort(lst):
    _merge_sort(lst, 0, len(lst) - 1)


li = list(range(2000))
random.shuffle(li)
# print(li)
merge_sort(li)
print(li)
