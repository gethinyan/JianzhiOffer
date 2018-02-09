# -*- coding:utf-8 -*-
# 题目: 替换空格


class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        result = ''
        for index in s:
            if index == ' ':
                result += '%20'
            else:
                result += index
        return result


obj = Solution()
print(obj.replaceSpace('We Are Happy'))
