# -*- coding:utf-8 -*-
# 题目: 顺时针打印矩阵


class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        lenRow = len(matrix)
        lenCol = len(matrix[0])
        print(lenRow, lenCol)
        i, j, step = 0, 0, 1
        startRow, startCol = 0, 0
        result = []
        while lenRow > 0 and lenCol > 0:
            while (step == 1 and j < lenCol + startCol - 1) or (step == -1 and j > startCol):
                result.append(matrix[i][j])
                j += step
            if step == -1:
                startCol += 1
            lenRow -= 1
            while (step == 1 and i < lenRow + startRow) or (step == -1 and i > startRow + 1):
                result.append(matrix[i][j])
                i += step
            if step == -1:
                startRow += 1
            lenCol -= 1
            step = -step
        result.append(matrix[i][j])
        return result


obj = Solution()
print(obj.printMatrix([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16],
]))
