# -*- coding:utf-8 -*-
# 题目: 树的子结构


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        if not pRoot1 or not pRoot2:
            return False
        return self.isSubtree(pRoot1, pRoot2) or self.HasSubtree(pRoot1.left, pRoot2) or self.HasSubtree(pRoot1.right, pRoot2)

    def isSubtree(self, sourceTree, targetTree):
        if not targetTree:
            return True
        if not sourceTree or sourceTree.val != targetTree.val:
            return False
        return self.isSubtree(sourceTree.left, targetTree.left) and self.isSubtree(sourceTree.right, targetTree.right)
