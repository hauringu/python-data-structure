# -*- coding: utf-8 -*- 
# @Time : 2021/4/21 15:16 
# @Author : HGuoo 
# @File : deque_test.py


from collections import deque


# 双向队列
# append队尾入队 popleft队首出队  appendleft队首入队 pop队尾出队
# 队满时队首自动出队
def tail(n):
    with open('abc.txt', 'r') as f:
        q = deque(f, n)
        for line in q:
            print(line, end='')


tail(5)
