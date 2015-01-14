'''
 Given a linked list, swap every two adjacent nodes and return its head.

For example,
Given 1->2->3->4, you should return the list as 2->1->4->3.

Your algorithm should use only constant space. You may not modify the values in the list, only nodes itself can be changed.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 递归的code更简洁. 不过有stack space
class Solution:
    # @param a ListNode
    # @return a ListNode
    def swapPairs(self, h):
        if not h or not h.next: return h
        n = h.next
        h.next = self.swapPairs(h.next.next)
        n.next = h
        return n



'''
class Solution:
    # @param a ListNode
    # @return a ListNode
    def swapPairs(self, head):
        dummy = ListNode(0)
        pre, dummy.next, last = dummy, head, head
        while last and last.next:  #考虑操纵2个node.这是必须的。
            cur = last.next
            last.next = cur.next
            cur.next = pre.next
            pre.next = cur
            #以上连环
            pre = last       #与reverse linkedlist 区别。  不断更新pre, last
            last = last.next  #普通的逆转，pre和last不会变的。。
        return dummy.next
'''