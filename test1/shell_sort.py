# -*- coding: utf-8 -*- 
# @Time : 2021/4/7 15:24 
# @Author : HGuoo 
# @File : shell_sort.py
import random
import copy
from test1.cal_time import *
from test1.sort import *

def insert_sort_gap(li, gap):
    for i in range(gap, len(li)):
        j = i - gap
        tmp = li[i]
        while j >= 0 and li[j] > tmp:
            li[j + gap] = li[j]
            j -= gap
        li[j + gap] = tmp

@cal_time
def shell_sort(li):
    d = len(li) // 2
    while d >= 1:
        insert_sort_gap(li, d)
        d //= 2


lst = list(range(10000))
random.shuffle(lst)
lst2 = copy.deepcopy(lst)
shell_sort(lst)
insert_sort(lst2)
# print(lst2)
# print(lst)
