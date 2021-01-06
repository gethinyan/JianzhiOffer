# -*- coding:utf-8 -*-
# 题目: 字符串的排列


class Solution:
    def Permutation(self, ss):
        # write code here
        if len(ss) == 0:
            return []
        if len(ss) == 1:
            return [ss]
        ret = []
        l = list(ss)
        l.sort()
        ss = "".join(l)
        previous = None
        for i in range(len(ss)):
            if previous == ss[i]:
                continue
            else:
                previous = ss[i]
            res = self.Permutation(ss[:i] + ss[i + 1:])
            for k in res:
                ret.append(ss[i:i + 1] + k)
        return ret


obj = Solution()
print(obj.Permutation('abcd'))
