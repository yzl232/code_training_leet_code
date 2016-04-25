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
            cur = cur.next.next

        cur = h
        while cur:      # # copy random pointers
            if cur.random: cur.next.random = cur.random.next
            cur = cur.next.next

        cur = h; cur2 = h2 = h.next
        while cur and cur2:  # choose next pointers . decouple the list
            cur.next, cur2.next = cur2.next, (cur2.next.next if cur2.next else None)
            cur, cur2 = cur.next, cur2.next
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
        d = {None:None};  x = head
        while x:
            d[x] = RandomListNode(x.label)
            x = x.next
        x = head
        while x:
            d[x].next = d[x.next]
            d[x].random = d[x.random]
            x = x.next
        return d[head]
'''