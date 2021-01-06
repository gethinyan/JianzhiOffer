# -*- coding:utf-8 -*-
# 题目: 反转链表


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        if pHead is None or pHead.next is None:
            return pHead
        resultNode = ListNode(pHead.val)
        while pHead.next is not None:
            curNode = ListNode(pHead.next.val)
            curNode.next = resultNode
            pHead = pHead.next
            resultNode = curNode
        return resultNode


head = ListNode(1)
nodeArr = [2, 3, 4, 5]
for item in nodeArr:
    curNode = ListNode(item)
    head.next = curNode
obj = Solution()
print(obj.ReverseList(head))
