'''
 Reverse a linked list from position m to n. Do it in-place and in one-pass.

For example:
Given 1->2->3->4->5->NULL, m = 2 and n = 4,

return 1->4->3->2->5->NULL.

Note:
Given m, n satisfy the following condition:
1 ≤ m ≤ n ≤ length of list.

'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @param m, an integer
    # @param n, an integer
    # @return a ListNode
    def reverseBetween(self, h, m, n):
        if not h: return
        dummy = ListNode(0)
        dummy.next = h;  pre = dummy
        for i in range(m-1):   pre = pre.next
        last, cur= pre.next, pre.next.next
        for i in range(n-m):
            last.next = cur.next
            cur.next = pre.next
            pre.next = cur
            cur = last.next
        return dummy.next