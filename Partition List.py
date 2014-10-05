'''
Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

For example,
Given 1->4->3->2->5->2 and x = 3,
return 1->2->2->4->3->5. 
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for singly-linked list.

class Solution:
    # @param head, a ListNode
    # @param x, an integer
    # @return a ListNode
    def partition(self, head, x):
        dummy = ListNode(0); pre=dummy; dummy.next = head
        big = head
        while big and big.val <x:
            big = big.next
            pre = pre.next
        if not big: return dummy.next
        cur = big.next; last = big
        while cur:
            if cur.val>=x:
                last = cur
                cur = cur.next
            else:
                last.next = cur.next
                cur.next = big
                pre.next = cur
                pre = cur
                cur = last.next
        return dummy.next



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution1:
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
        
        
        