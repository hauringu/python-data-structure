# -*- coding: utf-8 -*- 
# @Time : 2021/6/22 16:27 
# @Author : HGuoo 
# @File : 背包问题.py

# 一个小偷发现n个商品，第i个商品值v[i]元，重w[i]千克，小偷背包只能装W千克的物品，怎么样拿价值最高
# 0-1背包：一个商品只能拿或不拿，不能多次拿。例如金条
# 分数背包：一个商品可以拿走部分。例如金沙


def binary_package(n, w):
    pass


goods = [(60, 10), (100, 20), (120, 30)]  # (v,w)
goods.sort(key=lambda x: x[0] / x[1], reverse=True)


# 分数背包
def fractional_backpack(goods, w):
    m = [0 for _ in range(len(goods))]
    for i, (value, weight) in enumerate(goods):
        if w >= weight:
            m[i] = 1
            w -= weight
        else:
            m[i] = w / weight
            w = 0
            break
    return m


print(fractional_backpack(goods, 25))
