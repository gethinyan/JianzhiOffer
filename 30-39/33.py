# -**- coding:utf-8 -**-
# 题目: 丑数


class Solution:
    def GetUglyNumber_Solution(self, index):
        # write code here
        if not index or index <= 0:
            return 0
        uglyList = [1]
        indexTwo, indexThree, indexFive = 0, 0, 0
        while index > 1:
            uglyNum = min(uglyList[indexTwo] * 2, uglyList[indexThree] * 3, uglyList[indexFive] * 5)
            uglyList.append(uglyNum)
            if uglyNum % 2 == 0:
                indexTwo += 1
            if uglyNum % 3 == 0:
                indexThree += 1
            if uglyNum % 5 == 0:
                indexFive += 1
            index -= 1
        return uglyList[-1]

obj = Solution()
print(obj.GetUglyNumber_Solution(11))
