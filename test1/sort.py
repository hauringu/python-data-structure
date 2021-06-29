# -*- coding: utf-8 -*- 
# @Time : 2021/3/16 16:35 
# @Author : HGuoo 
# @File : sort.py

import random
import copy
from test1.cal_time import *


@cal_time
def bubble_sort(li):
    for i in range(len(li) - 1):
        exchange = False
        for j in range(len(li) - i - 1):
            if li[j] > li[j + 1]:
                li[j], li[j + 1] = li[j + 1], li[j]
                exchange = True
        if not exchange:
            return


@cal_time
def select_sort_simple(li):
    for i in range(len(li)):
        min_index = i
        for j in range(i + 1, len(li)):
            if li[min_index] > li[j]:
                min_index = j
        if min_index != i:
            li[i], li[min_index] = li[min_index], li[i]


@cal_time
def insert_sort(lst):
    for i in range(1, len(lst)):
        j = i - 1
        temp = lst[i]
        while j >= 0 and temp < lst[j]:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = temp


def _quick_sort_1(lst, left, right):
    l = left
    r = right
    temp = lst[left]
    while l < r:
        while lst[r] > temp and l < r:
            r -= 1
        if l < r:
            lst[l] = lst[r]
            l += 1
        while lst[l] < temp and l < r:
            l += 1
        if l < r:
            lst[r] = lst[l]
            r -= 1
    lst[l] = temp
    if l > left + 1:
        _quick_sort_1(lst, left, l - 1)
    if l < right - 1:
        _quick_sort_1(lst, l + 1, right)


def partition(lst, left, right):
    i = random.randint(left, right)
    lst[left], lst[i] = lst[i], lst[left]
    temp = lst[left]
    while left < right:
        while left < right and lst[right] >= temp:
            right -= 1
        lst[left] = lst[right]
        while left < right and lst[left] <= temp:
            left += 1
        lst[right] = lst[left]
    lst[left] = temp
    return left


def _quick_sort_2(lst, left, right):
    if left < right:
        mid = partition(lst, left, right)
        _quick_sort_2(lst, left, mid - 1)
        _quick_sort_2(lst, mid + 1, right)


@cal_time
def quick_sort_1(lst):
    _quick_sort_1(lst, 0, len(lst) - 1)


@cal_time
def quick_sort_2(lst):
    _quick_sort_2(lst, 0, len(lst) - 1)


# 堆向下调整（目标：大根堆）
def sift(lst, low, high):
    """

    :param lst: 堆列表
    :param low: 根节点
    :param high: 最后一个叶子节点
    """
    i = low
    j = 2 * i + 1  # 左子节点
    # tmp = lst[low]
    while j <= high:
        if j + 1 <= high and lst[j] < lst[j + 1]:  # 如果右子节点大于左子节点，j指向右子节点
            j = j + 1
        if lst[j] > lst[i]:
            lst[i], lst[j] = lst[j], lst[i]
            i = j  # 向下一层
            j = 2 * i + 1
        else:  # 没有比根大的子节点了
            # lst[i] = tmp # 优化为while调出后执行
            break
    # lst[i] = tmp  # j超出最大高度了，i为叶子节点


# 堆排序
def heap_sort(lst):
    n = len(lst)
    for i in range(n // 2 - 1, -1, -1):  # n//2-1 = (n-2)//2为最后一个节点的父节点索引
        sift(lst, i, n - 1)  # n-1为整个堆的最后一个叶子节点  所以也可以看作每个子堆的最后一个子节点 用于判断越界
    # 堆构造完了
    for i in range(n - 1, -1, -1):
        lst[0], lst[i] = lst[i], lst[0]
        sift(lst, 0, i - 1)


# 计数排序，O(n)，知道取值范围的一定数量的数排序
def count_sort(lst, max_count=100):
    count = [0 for _ in range(max_count + 1)]
    for val in lst:
        count[val] += 1
    lst.clear()
    for ind, val in enumerate(count):
        for i in range(val):
            lst.append(ind)


# 桶排序
def bucket_sort(lst, n=100, max_num=10000):
    """

    :param lst: 待排序列表
    :param n: 桶数量
    :param max_num: 元素最大值
    """
    bucket_li = [[] for _ in range(n)]
    for i in lst:
        idx = min(i // (max_num // n), n - 1)
        bucket_li[idx].append(i)
        for j in range(len(bucket_li[idx]) - 1, 0, -1):
            if bucket_li[idx][j] < bucket_li[idx][j - 1]:
                bucket_li[idx][j], bucket_li[idx][j - 1] = bucket_li[idx][j - 1], bucket_li[idx][j]
    li.clear()
    for buc in bucket_li:
        li.extend(buc)


# 基数排序(依次从个位到最高位分桶取回)
def radix_sort(lst):
    max_num = max(lst)
    it = 0
    while 10 ** it <= max_num:
        bucket = [[] for _ in range(10)]
        for i in lst:
            digit = (i // 10 ** it) % 10
            bucket[digit].append(i)
        lst.clear()
        for buc in bucket:
            lst.extend(buc)
        it += 1


li = [random.randint(0, 100) for _ in range(100)]

# li = list(range(100))
random.shuffle(li)
print(li)
radix_sort(li)
print(li)
# li2 = copy.deepcopy(li)
# heap_sort(li)
# print(li)
# print(li2)
