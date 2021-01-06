# -*- coding:utf-8 -*-
# 题目: 对称的二叉树
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def isSymmetrical(self, pRoot):
        # write code here
        if not pRoot:
            return True
        if not pRoot.left and pRoot.right:
            return False
        if pRoot.left and not pRoot.right:
            return False
        return self.isSame(pRoot.left, pRoot.right)

    def isSame(self, p1, p2):
        if not p1 and not p2:
            return True
        if p1 and p2 and p1.val == p2.val:
            return self.isSame(p1.left, p2.right) and self.isSame(p1.right, p2.left)
        return False
