# -*- coding: utf-8 -*- 
# @Time : 2021/6/23 15:27 
# @Author : HGuoo 
# @File : 活动选择问题.py


# 假设有n个活动，这些活动要占用同一片场地，而场地在某一时刻只能供一个活动使用
# 活动开始时间s[i]结束时间f[i] [s[i], f[i])左闭右开
# 怎么安排能使举办的活动数最多
# 贪心结论： 最先结束的活动一定在最优解里
# 证明：设a为最先结束的活动，b为最优解里最先结束的活动
# 如果a != b, a一定比b先结束， 所以a替换掉最优解里的b也不会与最优解里的其他活动有交集，所以替换后的解也是最优解， 所以最优解里的b=a
activity = [(1, 4), (3, 5), (0, 6), (5, 7), (3, 9), (5, 9), (6, 10), (8, 11), (8, 12), (2, 14), (12, 16)]


def select_activity(activity):
    activity.sort(key=lambda x: x[1])
    act = [activity[0]]
    for i in activity:
        if i[0] >= act[-1][1]:
            act.append(i)
    print(act)


select_activity(activity)
