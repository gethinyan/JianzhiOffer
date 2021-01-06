# -*- coding:utf-8 -*-
# 题目: 数组中的逆序对


class Solution:
    def __init__(self):
        self.count = 0

    def InversePairs(self, data):
        # write code here
        if len(data) < 2:
            return 0
        self.mergeSort(data)
        return self.count % 1000000007

    def mergeSort(self, numList):
        length = len(numList)
        if length < 2:
            return numList
        middle = length // 2
        leftList = self.mergeSort(numList[:middle])
        rightList = self.mergeSort(numList[middle:])
        leftLength = len(leftList)
        rightLength = len(rightList)
        mergedList = []
        i, j = 0, 0
        while i < leftLength and j < rightLength:
            if leftList[i] < rightList[j]:
                mergedList.append(leftList[i])
                i += 1
            # 当左边的大于右边的时候，表示左边（已排序）所有的元素都大于右边
            else:
                mergedList.append(rightList[j])
                j += 1
                self.count += leftLength - i

        return mergedList + leftList[i:] + rightList[j:]


obj = Solution()
print(obj.InversePairs([1, 2, 3, 4, 5, 6, 7, 0]))
