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
            if cur.random: cur.next.random = cur.random.next
            cur = cur.next.next

        cur = h
        h2 = h.next
        while cur:  # choose next pointers . decouple the list
            t = cur.next
            cur.next = t.next  # Alternating split of a given Singly Linked List
            if t.next:   t.next = t.next.next     # 举例就好  1, 2, 3, (4)  .   1=3,  2=4,   # 12
            cur = cur.next
        return h2


'''
# clone list with random node 用到了
class Solution:
    def splitAl(self, h):
        cur = h
        h2 = h.next
        while cur:  # choose next pointers . decouple the list
            t = cur.next
            cur.next = t.next
            if t.next:   t.next = t.next.next     # 1, 2, 3, (4)  .   1=3,  2=4
            cur = cur.next
        return h2
'''