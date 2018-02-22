# -*- coding:utf-8 -*-
# 题目: 左旋转字符串


class Solution:
    def LeftRotateString(self, s, n):
        # write code here
        if not s:
            return s
        n = n % len(s)
        i = -1
        for i in range(n):
            s += s[i]
        return s[i + 1:]


obj = Solution()
print(obj.LeftRotateString('abcdefg', 0))
