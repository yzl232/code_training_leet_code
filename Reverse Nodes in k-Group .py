'''
 Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

You may not alter the values in the nodes, only nodes itself may be changed.

Only constant memory is allowed.

For example,
Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5
'''

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
        dummy.next , cur, i, pre = head, head, 0, dummy
        while cur:
            i+=1
            if i%k==0:
                pre = self.reverse(pre, cur.next)  #每次reverse完就更新pre, cur
                cur = pre.next
            else:  cur = cur.next  #否则啥也不做。。只是继续next加1
        return dummy.next

    def reverse(self, pre, right):      # exclusively 因为exclusive最好操作
        last = pre.next
        cur = last.next
        while cur != right:
            last.next = cur.next
            cur.next = pre.next
            pre.next = cur
            cur = last.next
        return last