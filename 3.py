# -*- coding:utf-8 -*-
# 题目: 从尾到头打印链表


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 返回从尾部到头部的列表值序列，例如[1, 2, 3]
    def printListFromTailToHead(self, listNode):
        # write code here
        if listNode is None:
            return []
        result = []
        while listNode is not None:
            result.append(listNode.val)
            listNode = listNode.next
        return result[::-1]


oListNode = ListNode(3)
oListNode.next = ListNode(2)
oListNode.next.next = ListNode(1)
obj = Solution()
print(obj.printListFromTailToHead(oListNode))
