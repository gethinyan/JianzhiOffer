# -*- coding:utf-8 -*-
# 题目： 从上往下打印二叉树


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        # write code here
        if not root:
            return []
        nodeList = []
        result = []
        nodeList.append(root)
        while nodeList:
            curNode = nodeList.pop(0)
            result.append(curNode.val)
            if curNode.left:
                nodeList.append(curNode.left)
            if curNode.right:
                nodeList.append(curNode.right)
        return result


head = TreeNode(1)
head.left = TreeNode(2)
head.right = TreeNode(3)
obj = Solution()
print(obj.PrintFromTopToBottom(head))
