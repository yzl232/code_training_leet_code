'''
Given a list, rotate the list to the right by k places, where k is non-negative.

For example:
Given 1->2->3->4->5->NULL and k = 2,
return 4->5->1->2->3->NULL.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def rotateRight(self, h, k):
        if not h or k==0: return h
        l = 1; p = h
        while p.next:
            p = p.next; l+=1
        p.next = h   #连成环
        for i in range(l- k%l):   p = p.next
        h, p.next = p.next, None   #找到，断开
        return h