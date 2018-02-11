# -*- coding:utf-8 -*-
# 题目: 数值的整数次方


class Solution:
    def Power(self, base, exponent):
        # write code here
        result = 1
        if exponent == 0:
            return 1
        if exponent < 0:
            base = 1 / base
            exponent = -exponent
        for i in range(exponent):
            result *= base
        return result


obj = Solution()
print(obj.Power(1.5, 4))
