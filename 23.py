# -*- coding:utf-8 -*-
# 题目： 二叉搜索树的后序遍历序列


class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        if not sequence:
            return False
        if len(sequence) <= 1:
            return True
        lastItem = sequence[-1]
        index = 0
        while sequence[index] < lastItem:
            index += 1
        for i in range(index, len(sequence)):
            if sequence[i] < lastItem:
                return False
        leftVerify = True
        rightVerify = True
        if len(sequence[:index]):
            leftVerify = self.VerifySquenceOfBST(sequence[:index])
        if len(sequence[index:len(sequence) - 1]):
            rightVerify = self.VerifySquenceOfBST(sequence[index:len(sequence) - 1])
        return leftVerify and rightVerify


obj = Solution()
print(obj.VerifySquenceOfBST([1, 2, 4, 3]))
