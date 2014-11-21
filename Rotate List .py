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
    def rotateRight(self, head, k):
        if not head or k==0: return head
        l = 1; p = head
        while p.next:
            p = p.next
            l+=1
        step = l- k%l
        p.next = head
        for i in range(step):
            p = p.next
        head = p.next
        p.next = None
        return head