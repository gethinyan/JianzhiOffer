# -*- coding:utf-8 -*-
# 题目: 把二叉树打印成多行
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    # 返回二维列表[[1,2],[4,5]]
    def Print(self, pRoot):
        # write code here
        if not pRoot:
            return []
        res = []
        nodeList = [pRoot]
        while nodeList:
            tmpList = []
            tmpRes = []
            while nodeList:
                tmpNode = nodeList.pop(0)
                if tmpNode:
                    tmpRes.append(tmpNode.val)
                    tmpList.append(tmpNode.left)
                    tmpList.append(tmpNode.right)
            nodeList = tmpList
            if tmpRes:
                res.append(tmpRes)
        return res
