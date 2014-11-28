# encoding=utf-8
'''
Write a program to find the node at which the intersection of two singly linked lists begins.

For example, the following two linked lists:

A:          a1 → a2
                   ↘
                     c1 → c2 → c3
                   ↗
B:     b1 → b2 → b3

begin to intersect at node c1.

Notes:

    If the two linked lists have no intersection at all, return null.
    The linked lists must retain their original structure after the function returns.
    You may assume there are no cycles anywhere in the entire linked structure.
    Your code should preferably run in O(n) time and use only O(1) memory.



最简单的是用hashtable
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param two ListNodes
    # @return the intersected ListNode
    def getIntersectionNode(self, headA, headB):
        l1 = self.getCount(headA)
        l2 = self.getCount(headB)
        diff = abs(l1-l2)
        if l1<l2:  headB, headA = headA, headB
        for i in range(diff):
            headA = headA.next
        while headA and headB:
            if headA==headB: return headA
            headA = headA.next
            headB = headB.next

    def getCount(self, head):
        count = 0
        while head:
            head= head.next
            count+=1
        return count