# -*- coding: utf-8 -*- 
# @Time : 2021/4/30 15:31 
# @Author : HGuoo 
# @File : bstree_test.py

import tree_struct
from tree_struct.tree_test import *


class BiTreeNode:
    def __init__(self, data):
        self.data = data
        self.lchild = None
        self.rchild = None
        self.parent = None


class BST:
    def __init__(self, li=None):
        self.root = None
        if li:
            for i in li:
                self.insert_without_rec(i)

    def insert(self, node, val):
        if not node:
            node = BiTreeNode(val)
        elif val < node.data:
            node.lchild = self.insert(node.lchild, val)
            node.lchild.parent = node
        elif val > node.data:
            node.rchild = self.insert(node.rchild, val)
            node.rchild.parent = node
        return node

    def insert_without_rec(self, val):
        if not self.root:
            self.root = BiTreeNode(val)
            return
        cur = self.root
        node = cur
        while cur:
            node = cur
            if val < cur.data:
                cur = cur.lchild
            elif val > cur.data:
                cur = cur.rchild
            else:
                return
        if val < node.data:
            node.lchild = BiTreeNode(val)
            node.lchild.parent = node
        elif val > node.data:
            node.rchild = BiTreeNode(val)
            node.rchild.parent = node
        else:
            return

    def query_no_rec(self, val):
        cur = self.root
        while cur:
            if val == cur.data:
                return cur
            elif val < cur.data:
                cur = cur.lchild
            elif val > cur.data:
                cur = cur.rchild
        return None

    def __remove_node_1(self, node):
        # 1: node是叶子节点
        if not node.parent:
            self.root = None
            return
        if node.parent == node.parent.lchild:
            node.parent.lchild = None
        else:
            node.parent.rchild = None

    def __remove_node_2_1(self, node):
        # 2.1: node只有左子树
        if not node.parent:
            self.root = None
            return
        if node == node.parent.lchild:
            node.parent.lchild = node.lchild
            node.lchild.parent = node.parent
        else:
            node.parent.rchild = node.lchild
            node.lchild.parent = node.parent

    def __remove_node_2_2(self, node):
        # 2.1: node只有右子树
        if not node.parent:
            self.root = None
            return
        # node 是左子树
        if node == node.parent.lchild:
            node.parent.lchild = node.rchild
            node.rchild.parent = node.parent
        # node 是右子树
        else:
            node.parent.rchild = node.rchild
            node.rchild.parent = node.parent


    def delete(self,val):
        # 空树
        if not self.root:
            return
        node = self.query_no_rec(val)
        # 不存在
        if not node:
            return
        if not node.lchild and not node.rchild:
            self.__remove_node_1(node)
        elif node.lchild and not node.rchild:
            self.__remove_node_2_1(node)
        elif not node.lchild and node.rchild:
            self.__remove_node_2_2(node)
        else:
            # node有两个子树，删除node的右子树最小的节点（最多有一个右子树的节点），将node替换为它
            min_node = node.rchild
            while min_node.lchild:
                min_node = min_node.lchild
            node.data = min_node.data
            if min_node.rchild:
                self.__remove_node_2_2(min_node)
            else:
                self.__remove_node_1(min_node)





# a = BiTreeNode(3)
# b = BiTreeNode(1)
# c = BiTreeNode(8)
# d = BiTreeNode(5)
# e = BiTreeNode(12)
# a.lchild = b
# a.rchild = c
# c.lchild = d
# d.rchild = e
#
# bst = BST()
# bst.root = a
# pre_order(bst.root)
#
# # bst.insert(bst.root, 4)
# bst.insert_without_rec(4)
# print()
# pre_order(bst.root)
# print()
# in_order(bst.root)
# print()
#
# print(bst.query_no_rec(8))
# print()
#
#
# bst2 = BST([2,5,3,1,4,7,6,9])
# pre_order(bst2.root)
# print()
# in_order(bst2.root)
# print()
# bst2.delete(7)
# pre_order(bst2.root)