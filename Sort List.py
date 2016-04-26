'''
Sort a linked list in O(n log n) time using constant space complexity.
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def sortList(self, h):
        if not h or not h.next: return h
        fast = slow = h
        while fast.next and fast.next.next:  #  fast.next and fast.next.next.   举例 1->2   就不行了.
            slow, fast = slow.next, fast.next.next
        h2 = slow.next
        slow.next = None
        return self.mergeTwoLists(self.sortList(h), self.sortList(h2))

    def mergeTwoLists(self, l1, l2):
        dummy = ListNode(-1); cur = dummy
        while l1 and l2:
            if l1.val <= l2.val:
                cur.next = l1
                l1, cur = l1.next, cur.next
            else:
                cur.next = l2
                l2, cur = l2.next, cur.next
        cur.next = l1 or l2
        return dummy.next