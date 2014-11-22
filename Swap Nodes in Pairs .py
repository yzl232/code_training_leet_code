'''
 Given a linked list, swap every two adjacent nodes and return its head.

For example,
Given 1->2->3->4, you should return the list as 2->1->4->3.

Your algorithm should use only constant space. You may not modify the values in the list, only nodes itself can be changed.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param a ListNode
    # @return a ListNode
    def swapPairs(self, head):
        dummy = ListNode(-1); 
        pre = dummy; pre.next = head; last = head
        while last and last.next:
            cur = last.next
            last.next = cur.next
            cur.next = pre.next
            pre.next = cur
            pre = last
            last = last.next
        return dummy.next