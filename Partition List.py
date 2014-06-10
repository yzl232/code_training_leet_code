# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @param x, an integer
    # @return a ListNode
    def partition(self, head, x):
        left_dummy = ListNode(0); right_dummy = ListNode(0)
        leftCur = left_dummy; rightCur = right_dummy; cur = head
        while cur:
            if cur.val < x:
                leftCur.next = cur
                leftCur = cur
            else:
                rightCur.next = cur
                rightCur = cur
            cur = cur.next
        rightCur.next = None
        leftCur.next = right_dummy.next
        return left_dummy.next