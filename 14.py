# -*- coding:utf-8 -*-
# 题目: 链表中倒数第k个结点


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        if head is None or k == 0:
            return None
        preHead = head
        for i in range(k - 1):
            if head.next is not None:
                head = head.next
            else:
                return None
        while head.next is not None:
            head = head.next
            preHead = preHead.next
        return preHead


head = ListNode(1)
nodeArr = [2, 3, 4, 5]
for item in nodeArr:
    curNode = ListNode(item)
    head.next = curNode
obj = Solution()
print(obj.FindKthToTail(head, 1))
