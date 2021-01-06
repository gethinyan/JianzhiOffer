# -*- coding:utf-8 -*-
# 题目: 扑克牌顺子


class Solution:
    def IsContinuous(self, numbers):
        # write code here
        if not numbers:
            return False
        minNum = 0
        maxNum = 0
        for num in numbers:
            if num != 0:
                if num < minNum or minNum == 0:
                    minNum = num
                if num > maxNum:
                    maxNum = num
        if maxNum - minNum >= 5:
            return False
        numbers = sorted(numbers)
        for i in range(len(numbers) - 1):
            if numbers[i] == numbers[i + 1] and numbers[i] != 0:
                return False
        return True


obj = Solution()
print(obj.IsContinuous([1, 3, 2, 5, 4]))
