# -*- coding:utf-8 -*-
# 题目: 按之字形打印二叉树


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def Print(self, pRoot):
        # write code here
        if not pRoot:
            return []
        res = []
        reverse = True
        nodeList = [pRoot]
        while nodeList:
            tmpList = []
            tmpRes = []
            while nodeList:
                tmpNode = nodeList.pop(0)
                if tmpNode:
                    tmpRes.append(tmpNode.val)
                    if reverse == True:
                        tmpList.append(tmpNode.left)
                        tmpList.append(tmpNode.right)
                    if reverse == False:
                        tmpList.append(tmpNode.right)
                        tmpList.append(tmpNode.left)
            nodeList = tmpList[::-1]
            if tmpRes:
                res.append(tmpRes)
            if reverse == True:
                reverse = False
            else:
                reverse = True
        return res


head = TreeNode(1)
head.right = TreeNode(2)
head.left = TreeNode(3)
head.left.left = TreeNode(4)
head.left.right = TreeNode(5)
head.right.left = TreeNode(6)
head.right.right = TreeNode(7)
obj = Solution()
print(obj.Print(head))
