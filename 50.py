# -*- coding:utf-8 -*-
# 题目: 数组中重复的数字


class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        # write code here
        res = []
        for each in numbers:
            if each in res:
                duplication[0] = each
                return True
            else:
                res.append(each)
        return False


obj = Solution()
print(obj.duplicate([2, 3, 1, 0, 2, 5, 3, 2], [0]))
