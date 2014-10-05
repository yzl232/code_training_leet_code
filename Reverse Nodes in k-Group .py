# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def reverseKGroup(self, head, k):
        dummy = ListNode(0)
        dummy.next = head
        cur = head
        i = 0
        pre = dummy
        while cur:
            i+=1
            if i%k ==0:
                pre = self.reverse(pre, cur.next)
                cur = pre.next
            else:
                cur = cur.next
        return dummy.next

    def reverse(self, pre, right):      # exclusively
        last = pre.next; cur = last.next
        while cur != right:
            last.next = cur.next
            cur.next = pre.next
            pre.next = cur
            cur = last.next
        return last