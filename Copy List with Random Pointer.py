'''
 A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

Return a deep copy of the list.
'''
# Definition for singly-linked list with a random pointer.
# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None
class Solution:
    # @param head, a RandomListNode
    # @return a RandomListNode
    def copyRandomList(self, head):
        if not head: return

        cur = head
        while cur: # insert additional nodes
            tmp = RandomListNode(cur.label)
            tmp.next = cur.next
            cur.next = tmp
            cur = tmp.next

        cur = head
        while cur:      # # copy random pointers
            temp = cur.next
            if cur.random: temp.random = cur.random.next
            cur = temp.next

        cur = head
        head2 = head.next
        while cur:  # choose next pointers . decouple the list
            temp = cur.next
            cur.next = temp.next
            if temp.next:   temp.next = temp.next.next
            cur = cur.next
        return head2
'''
# Definition for singly-linked list with a random pointer.
# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None
class Solution:
    # @param head, a RandomListNode
    # @return a RandomListNode
    def copyRandomList(self, head):
        if not head: return
        h, p = {}, head
        while p:
            h[p] = RandomListNode(p.label)
            p = p.next
        p = head
        while p:
            node = h[p]
            if p.next:  node.next = h[p.next]
            if p.random:  node.random = h[p.random]
            p = p.next
        return h[head]
'''