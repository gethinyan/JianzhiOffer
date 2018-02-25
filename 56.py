# -*- coding:utf-8 -*-
# 题目: 删除链表中重复的结点


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplication(self, pHead):
        # write code here
        if not pHead:
            return
        haed = pHead
        valDic = {}
        while haed is not None:
            if haed.val in valDic:
                valDic[haed.val] += 1
            else:
                valDic[haed.val] = 1
            haed = haed.next
        head = pHead
        while head.next:
            if valDic[head.next.val] > 1:
                head.next = head.next.next
            else:
                head = head.next
        if valDic[pHead.val] > 1:
            return pHead.next
        return pHead


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(3)
head.next.next.next.next = ListNode(4)
head.next.next.next.next.next = ListNode(4)
head.next.next.next.next.next.next = ListNode(5)
obj = Solution()
print(obj.deleteDuplication(head))
