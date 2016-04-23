'''
Given a linked list, remove the nth node from the end of list and return its head.

For example,

   Given linked list: 1->2->3->4->5, and n = 2.

   After removing the second node from the end, the linked list becomes 1->2->3->5.

Note:
Given n will always be valid.
Try to do this in one pass.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @return a ListNode
    def removeNthFromEnd(self, head, n):
        dummy=ListNode(0); dummy.next=head
        p1=p2=dummy
        for i in range(n): p1=p1.next
        while p1.next:   # 拿极端情况测试。比如n=5，移除第一个node
            p1, p2 =  p1.next, p2.next  #此时p2开始走。 保证了P2走length-n步
        p2.next=p2.next.next
        return dummy.next