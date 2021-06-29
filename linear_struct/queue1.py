# -*- coding: utf-8 -*- 
# @Time : 2021/4/21 14:32 
# @Author : HGuoo 
# @File : queue1.py

from collections import deque


class Queue:
    def __init__(self, size=100):
        self.queue = [0 for _ in range(size)]
        self.size = size
        self.rear = 0
        self.front = 0

    def push(self, element):
        if self.is_filled():
            raise IndexError("Queue is filled.")
        self.rear = (1 + self.rear) % self.size
        self.queue[self.rear] = element

    def pop(self):
        if self.is_empty():
            raise IndexError("Queue is empty.")
        self.front = (1 + self.front) % self.size
        return self.queue[self.front]

    def is_empty(self):
        return self.front == self.rear

    def is_filled(self):
        return (1 + self.rear) % self.size == self.front

    def is_contained(self, element):
        for i in self.queue:
            if i == element:
                return True
        return False


dirs = [
    lambda x, y: (x - 1, y),
    lambda x, y: (x + 1, y),
    lambda x, y: (x, y - 1),
    lambda x, y: (x, y + 1),
]

maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 1, 1, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]


def maze_path_q(maze, x1, y1, x2, y2):
    q = deque()
    q.append((x1, y1, -1))
    maze[x1][y1] = 2
    p = []
    while len(q) > 0:
        curNode = q.pop()
        p.append(curNode)
        if curNode[0] == x2 and curNode[1] == y2:
            break
        for dir in dirs:
            nextNode = dir(curNode[0], curNode[1])
            if maze[nextNode[0]][nextNode[1]] == 0:
                q.append((nextNode[0], nextNode[1], len(p) - 1))
                maze[nextNode[0]][nextNode[1]] = 2
    else:
        print("no path")
        return
    i = len(p) - 1
    while i > -1:
        print((p[i][0], p[i][1]))
        i = p[i][2]


maze_path_q(maze, 1, 1, 8, 8)
