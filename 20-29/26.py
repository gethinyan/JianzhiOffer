# -*- coding:utf-8 -*-
# 题目: 二叉搜索树与双向链表


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def Convert1(self, pRootOfTree):
        # write code here
        if not pRootOfTree:
            return
        pre = None
        self.convertHelper(pRootOfTree, pre)
        res = pRootOfTree
        while res.left:
            res = res.left
        return res

    def convertHelper(self, head, pre):
        if not head:
            return
        self.convertHelper(head.left, pre)
        head.left = pre
        if pre:
            pre.right = head
        pre = head
        self.convertHelper(head.right, pre)

    def Convert(self, pRootOfTree):
        # write code here
        if not pRootOfTree:
            return pRootOfTree
        if not pRootOfTree.left and not pRootOfTree.right:
            return pRootOfTree
        # 处理左子树
        self.Convert(pRootOfTree.left)
        left = pRootOfTree.left
        if left:
            while left.right:
                left = left.right
            pRootOfTree.left, left.right = left, pRootOfTree
        # 处理右子树
        self.Convert(pRootOfTree.right)
        right = pRootOfTree.right
        if right:
            while right.left:
                right = right.left
            pRootOfTree.right, right.left = right, pRootOfTree
        # 返回最小节点
        while pRootOfTree.left:
            pRootOfTree = pRootOfTree.left
        return pRootOfTree


head = TreeNode(10)
head.left = TreeNode(6)
head.right = TreeNode(14)
head.left.left = TreeNode(4)
head.left.right = TreeNode(8)
head.right.left = TreeNode(12)
head.right.right = TreeNode(16)
obj = Solution()
obj.Convert(head)
