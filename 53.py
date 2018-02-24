# -*- coding:utf-8 -*-
# 题目: 表示数值的字符串
import re


class Solution:
    # s字符串
    def isNumeric(self, s):
        # write code here
        return re.match(r'^[\+\-]?[0-9]*(\.[0-9]*)?([eE][\+\-]?[0-9]+)?$', s)
    # s字符串

    def isNumeric1(self, s):
        # write code here
        try:
            p = float(s)
            return True
        except:
            return False


obj = Solution()
print(obj.isNumeric('-1E-16'))
print(obj.isNumeric1('-1E-16'))
