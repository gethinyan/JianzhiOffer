# -*- coding:utf-8 -*-
# 题目: 第一个只出现一次的字符


class Solution:
    def FirstNotRepeatingChar(self, s):
        # write code here
        if not s:
            return -1
        sDic = {}
        for item in s:
            if item not in sDic:
                sDic[item] = 1
            else:
                sDic[item] += 1
        print(sDic)
        for i in range(len(s)):
            if sDic[s[i]] == 1:
                return i
        return -1


obj = Solution()
print(obj.FirstNotRepeatingChar('abcdabc'))
