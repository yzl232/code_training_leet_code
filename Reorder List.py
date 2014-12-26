
            
''''

 Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You must do this in-place without altering the nodes' values.

For example,
Given {1,2,3,4}, reorder it to {1,4,2,3}. 
''''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return nothing
    def reorderList(self, h):
        if not h or not h.next: return
        fast = slow = h
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        h2 = slow.next
        slow.next = None
        h2 = self.reverse(h2)
        while h and h2:
            t1 = h.next;  t2 = h2.next
            h.next = h2;   h2.next = t1
            h = t1;    h2 = t2

    def reverse(self, head):
        if not head: return
        dummy = ListNode(-1); dummy.next = head
        pre = dummy; last = head; cur = head.next
        while cur:
            last.next = cur.next
            cur.next = pre.next
            pre.next = cur
            cur = last.next
        return dummy.next