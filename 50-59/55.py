# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def EntryNodeOfLoop(self, pHead):
        # write code here
        tempList = []
        while pHead:
            if pHead in tempList:
                return pHead
            else:
                tempList.append(pHead)
            pHead = pHead.next
