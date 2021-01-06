# -*- coding:utf-8 -*-
# 题目： 栈的压入弹出序列


class Solution:
    def IsPopOrder(self, pushV, popV):
        # write code here
        if not pushV or len(pushV) != len(popV):
            return False
        stack = []
        for item in pushV:
            stack.append(item)
            while len(stack) and stack[-1] == popV[0]:
                stack.pop()
                popV.pop(0)
        if len(stack):
            return False
        return True


obj = Solution()
print(obj.IsPopOrder([1, 2, 3, 4, 5], [4, 5, 3, 2, 1]))
