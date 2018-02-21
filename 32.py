# -*- coding:utf-8 -*-
# 题目: 把数组排成最小的数


class Solution:
    def PrintMinNumber(self, numbers):
        # write code here
        if not numbers:
            return ''
        nums = map(str, numbers)
        nums.sort(lambda x, y: cmp(x + y, y + x))
        return ''.join(nums)


obj = Solution()
print(obj.PrintMinNumber([3, 32, 321]))
