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
    def reverseBetween(self, head, m, n):
        if head == None: return
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy

        
        for i in range(1, m):
            pre = pre.next
        last = pre.next
        cur = last.next
        for i in range(m, n):
            last.next = cur.next
            cur.next = pre.next
            pre.next = cur
            cur = last.next
        return dummy.next
            
            
        