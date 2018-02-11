# -*- coding:utf-8 -*-
# 题目: 合并两个排序的链表


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        resultNode = ListNode(1)
        head = resultNode
        while pHead1 is not None and pHead2 is not None:
            if pHead1.val < pHead2.val:
                curNode = ListNode(pHead1.val)
                pHead1 = pHead1.next
            else:
                curNode = ListNode(pHead2.val)
                pHead2 = pHead2.next
            resultNode.next = curNode
            resultNode = resultNode.next
        if pHead1 is not None:
            resultNode.next = pHead1
        if pHead2 is not None:
            resultNode.next = pHead2
        return head.next


head1 = ListNode(1)
head2 = ListNode(1)
nodeArr1 = [2, 3, 4, 5]
nodeArr2 = [2, 3, 4, 5]
for item in nodeArr1:
    curNode = ListNode(item)
    head1.next = curNode
for item in nodeArr2:
    curNode = ListNode(item)
    head2.next = curNode
obj = Solution()
print(obj.Merge(head1, head2))
