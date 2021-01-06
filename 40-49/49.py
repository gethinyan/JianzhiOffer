# -*- coding:utf-8 -*-
# 题目: 把字符串换成整数


class Solution:
    def StrToInt(self, s):
        # write code here
        try:
            return int(s)
        except Exception as e:
            return 0


obj = Solution()
print(obj.StrToInt('123'))
