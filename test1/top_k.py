# -*- coding: utf-8 -*- 
# @Time : 2021/4/2 14:34 
# @Author : HGuoo 
# @File : top_k.py
import random
import copy


# 堆向下调整（目标：小根堆）
def sift(lst, low, high):
    """

    :param lst: 堆列表
    :param low: 根节点
    :param high: 最后一个叶子节点
    """
    i = low
    j = 2 * i + 1
    tmp = lst[low]
    while j <= high:
        if j + 1 <= high and lst[j + 1] < lst[j]:
            j = j + 1
        if lst[j] < tmp:
            lst[i] = lst[j]
            i = j  # 向下一层
            j = 2 * i + 1
        else:
            break
    lst[i] = tmp


def top_k(lst, k):
    heap = lst[0:k]
    for i in range(k // 2 - 1, -1, -1):
        sift(heap, i, k - 1)
    for i in range(k, len(lst)):
        if heap[0] < lst[i]:
            heap[0] = lst[i]
            sift(heap, 0, k - 1)
    for i in range(k - 1, -1, -1):
        heap[i], heap[0] = heap[0], heap[i]
        sift(heap, 0, i - 1)
    return heap


ls = list(range(20))
random.shuffle(ls)
ls2 = copy.deepcopy(ls)
heap = top_k(ls, 5)
print(ls2)
print(heap)

