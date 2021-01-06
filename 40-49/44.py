# -*- coding:utf-8 -*-
# 题目: 翻转单词顺序列


class Solution:
    def ReverseSentence(self, s):
        # write code here
        if not s:
            return s
        L = s.split(' ')
        return ' '.join(L[::-1])


obj = Solution()
print(obj.ReverseSentence('student. a am I'));
