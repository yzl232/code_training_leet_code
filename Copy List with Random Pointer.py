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
    def copyRandomList(self, h):
        if not h: return

        cur = h
        while cur: # insert additional nodes
            t = RandomListNode(cur.label)
            t.next = cur.next
            cur.next = t
            cur = t.next

        cur = h
        while cur:      # # copy random pointers
            t = cur.next
            if cur.random: t.random = cur.random.next
            cur = t.next

        cur = h
        h2 = h.next
        while cur:  # choose next pointers . decouple the list
            t = cur.next
            cur.next = t.next
            if t.next:   t.next = t.next.next
            cur = cur.next
        return h2
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
        d, p = {None: None}, head
        while p:
            d[p] = RandomListNode(p.label)
            p = p.next
        p = head
        while p:
            p1 = d[p]
            p1.next = d[p.next]
            p1.random = d[p.random]
            p = p.next
        return d[head]
'''