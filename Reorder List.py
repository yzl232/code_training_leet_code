
            
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
    def reorderList(self, head):
        if not head or not head.next or not head.next.next: return
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        head2 = slow.next
        slow.next = None

        dummy = ListNode(0)
        pre = dummy; dummy.next = head2; last = head2
        cur = head2.next
        while cur:
            last.next = cur.next
            cur.next = pre.next
            pre.next = cur
            cur = last.next
        head2 = pre.next

        p1 = head; p2 = head2
        while p2 and p1:
            temp1 =p1.next
            temp2 = p2.next
            p1.next = p2
            p2.next = temp1

            p1 = temp1
            p2 = temp2
