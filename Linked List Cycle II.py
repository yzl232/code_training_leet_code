'''
 Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

Follow up:
Can you solve it without using extra space? 
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:  #http://fisherlei.blogspot.com/2013/11/leetcode-linked-list-cycle-ii-solution.html  X和K的关系是基于Y互补的。等于说，两个指针相遇以后，再往下走X步就回到Cycle的起点了
    # @param head, a ListNode
    # @return a list node
    def detectCycle(self, head):
        fast = slow = head
        while fast and fast.next :
            slow, fast = slow.next, fast.next.next
            if fast == slow:   break
        if not fast or not fast.next: return
        fast = head
        while fast!= slow:
            fast, slow = fast.next, slow.next
        return fast
