# -*- coding: utf-8 -*- 
# @Time : 2021/6/16 17:31 
# @Author : HGuoo 
# @File : avl_tree.py

from tree_struct.bstree_test import BiTreeNode, BST
from tree_struct.tree_test import pre_order, in_order


class AVLNode(BiTreeNode):
    def __init__(self, data):
        BiTreeNode.__init__(self, data)
        self.bf = 0


class AVLTree(BST):
    def __init__(self, li=None):
        BST.__init__(self, li)

    def rotate_left(self, p, c):
        s2 = c.lchild
        p.rchild = s2
        if s2:
            s2.parent = p
        c.lchild = p
        p.parent = c
        p.bf = 0
        c.bf = 0
        return c

    def rotate_right(self, p, c):
        s2 = c.rchild
        p.lchild = s2
        if s2:
            s2.parent = p
        c.rchild = p
        p.parent = c
        c.bf = 0
        p.bf = 0
        return c

    def rotate_right_left(self, p, c):
        # 先右旋
        g = c.lchild
        s3 = c.lchild.rchild
        c.lchild = s3
        if s3:
            s3.parent = c
        g.rchild = c
        c.parent = g
        # p.rchild = g
        # g.parent = p
        # 再左旋
        s2 = g.lchild
        p.rchild = s2
        if s2:
            s2.parent = p
        g.lchild = p
        p.parent = g
        # 更新bf
        if g.bf > 0:
            p.bf = 0
            c.bf = -1
        elif g.bf < 0:
            p.bf = 1
            c.bf = 0
        else:  # 插入的是g
            p.bf = 0
            c.bf = 0
        g.bf = 0
        return g

    def rotate_left_right(self, p, c):
        g = c.rchild
        s2 = g.lchild
        c.rchild = s2
        if s2:
            s2.parent = c
        g.lchild = c
        c.parent = c
        s3 = g.rchild
        p.lchild = s3
        if s3:
            s3.parent = p
        g.rchild = p
        p.parent = g
        # 更新bf
        if g.bf > 0:
            p.bf = -1
            c.bf = 0
        elif g.bf < 0:
            p.bf = 0
            c.bf = 1
        else:  # 插入的是g
            p.bf = 0
            c.bf = 0
        g.bf = 0
        return g

    def insert_without_rec(self, val):
        p = self.root
        if not p:
            self.root = AVLNode(val)
            self.root.bf = 0
            return
        while True:
            if val < p.data:
                if p.lchild:
                    p = p.lchild
                else:
                    p.lchild = AVLNode(val)
                    p.lchild.bf = 0
                    p.lchild.parent = p
                    # 记录插入节点的位置
                    node = p.lchild
                    break
            elif val > p.data:
                if p.rchild:
                    p = p.rchild
                else:
                    p.rchild = AVLNode(val)
                    p.rchild.bf = 0
                    p.rchild.parent = p
                    # 记录插入节点的位置
                    node = p.rchild
                    break
            else:
                return
        # 更新balance factor
        while node.parent:
            # 传递从左子树来
            if node.parent.lchild == node:
                if node.parent.bf > 0:
                    # 记录原先与当前需旋转子树相连的节点，一遍旋转后连回去
                    g = node.parent.parent
                    # 记录旋转前的子树根，用来判断其是父节点的左、右子树
                    x = node.parent
                    # 看node那边沉
                    if node.bf > 0:
                        n = self.rotate_right(node.parent, node)
                    else:
                        n = self.rotate_left_right(node.parent, node)

                elif node.parent.bf < 0:
                    # 父节点的高度不变
                    node.parent.bf = 0
                    break
                else:
                    node.parent.bf = 1
                    # 继续向上传递
                    node = node.parent
                    continue
            # 传递从右子树来
            else:
                if node.parent.bf > 0:
                    node.parent.bf = 0
                    break
                elif node.parent.bf < 0:
                    # 记录原先与当前需旋转子树相连的节点，一遍旋转后连回去
                    g = node.parent.parent
                    x = node.parent
                    # 看node那边沉
                    if node.bf > 0:
                        n = self.rotate_right_left(node.parent, node)
                    else:
                        n = self.rotate_left(node.parent, node)
                else:
                    node.parent.bf = -1
                    # 继续向上传递
                    node = node.parent
                    continue
            n.parent = g
            if g:
                if x == g.lchild:
                    g.lchild = n
                else:
                    g.rchild = n
            else:
                self.root = n
            break


t = AVLTree([1, 2, 3, 4, 5, 6, 7, 8, 9])
# t.insert_without_rec(1)
# t.insert_without_rec(2)
# t.insert_without_rec(3)
# t.insert_without_rec(4)
# t.insert_without_rec(5)
# t.insert_without_rec(6)
# t.insert_without_rec(7)
# t.insert_without_rec(8)
# t.insert_without_rec(9)
pre_order(t.root)
print()
in_order(t.root)
