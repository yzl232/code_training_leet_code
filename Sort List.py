# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def sortList(self, head):
        if not head or not head.next: return head
        fast = head; slow = head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        # break the list
        fast = slow
        slow = slow.next
        fast.next = None
        # recursion
        l1 = self.sortList(head)
        l2 = self.sortList(slow)
        return self.mergeTwoLists(l1, l2)

    def mergeTwoLists(self, l1, l2):
        dummy = ListNode(-1); cur = dummy
        while l1 and l2:
            if l1.val <= l2.val:
                cur.next = l1
                l1 = l1.next
                cur = cur.next
            else:
                cur.next = l2
                l2 = l2.next
                cur = cur.next
        if l1:
            cur.next = l1
        if l2:
            cur.next = l2
        return dummy.next