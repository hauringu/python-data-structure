# -*- coding: utf-8 -*- 
# @Time : 2021/4/20 15:13 
# @Author : HGuoo 
# @File : stack.py


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        return self.stack.pop()

    def get_top(self):
        if len(self.stack) == 0:
            return None
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0

    def is_contained(self, element):
        for i in self.stack:
            if element == i:
                return True
        return False


def brackets_match(s):
    match = {')': '(', ']': '[', '}': '{'}
    stack = Stack()
    for ch in s:
        if ch in {'(', '[', '{'}:
            stack.push(ch)
        elif ch in {')', ']', '}'}:
            if stack.is_empty():
                return False
            else:
                p = stack.pop()
                if match[ch] != p:
                    return False
    return stack.is_empty()


# print(brackets_match("[]{[(111)[]]}()"))


# 迷宫问题
def maze_path(maze, x1, y1, x2, y2):
    stack = Stack()
    stack.push((x1, y1))
    badPoint = Stack()
    while stack.get_top() != (x2, y2) and not stack.is_empty():
        x, y = stack.get_top()
        if x - 1 >= 0 and maze[x - 1][y] == 0 and not stack.is_contained((x - 1, y)) and not badPoint.is_contained(
                (x - 1, y)):
            stack.push((x - 1, y))
        elif y + 1 <= len(maze[0]) and maze[x][y + 1] == 0 and not stack.is_contained(
                (x, y + 1)) and not badPoint.is_contained((x, y + 1)):
            stack.push((x, y + 1))
        elif x + 1 <= len(maze) and maze[x + 1][y] == 0 and not stack.is_contained(
                (x + 1, y)) and not badPoint.is_contained((x + 1, y)):
            stack.push((x + 1, y))
        elif y - 1 >= 0 and maze[x][y - 1] == 0 and not stack.is_contained((x, y - 1)) and not badPoint.is_contained(
                (x, y - 1)):
            stack.push((x, y - 1))
        else:
            badPoint.push(stack.pop())
    if stack.is_empty():
        print("no path")
    return stack


dirs = [
    lambda x, y: (x - 1, y),
    lambda x, y: (x + 1, y),
    lambda x, y: (x, y - 1),
    lambda x, y: (x, y + 1),
]


def maze_path_2(maze, x1, y1, x2, y2):
    stack = []
    stack.append((x1, y1))
    maze[x1][y1] = 2
    while len(stack) > 0:
        curNode = stack[-1]
        if curNode[0] == x2 and curNode[1] == y2:
            for i in stack:
                print(i)
            return
        for dir in dirs:
            nextNode = dir(curNode[0], curNode[1])
            if maze[nextNode[0]][nextNode[1]] == 0:
                stack.append(nextNode)
                maze[nextNode[0]][nextNode[1]] = 2  # 走过的点
                break
        else:
            # maze[curNode[0]][curNode[1]] = 2
            stack.pop()
    else:
        print("no path")
        return


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

# path = maze_path(maze, 1, 1, 8, 8)
# for i in path.stack:
#     print(i)

maze_path_2(maze, 1, 1, 8, 8)
