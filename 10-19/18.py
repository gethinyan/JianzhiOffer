# -*- coding:utf-8 -*-
# 题目: 二叉树的镜像
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    # 返回镜像树的根节点
    def Mirror(self, root):
        # write code here
        if root is not None:
            root.left, root.right = root.right, root.left
            self.Mirror(root.right)
            self.Mirror(root.left)
        return root
