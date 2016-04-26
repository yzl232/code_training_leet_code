# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

'''
 Given a linked list, determine if it has a cycle in it.

Follow up:
Can you solve it without using extra space?
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a boolean
    def hasCycle(self, head):
        fast = slow = head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
            if slow==fast: return True
        return False
'''
#和decouple的部分很像。  while条件稍有不同。   因为我们要找h2 前面的node来裂开。

        fast = slow = head  #试验了一下。  必须是   while fast.next and fast.next.next
        while fast.next and fast.next.next:  #因为要对前面的节点进行裂开操作。 着了是 fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        head2 = slow.next
        slow.next = None

'''
