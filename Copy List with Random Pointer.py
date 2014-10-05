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
        mapNode = {}
        p = head
        while p:
            node = RandomListNode(p.label)
            mapNode[p] = node
            p = p.next
        p = head
        while p:
            node = mapNode[p]
            if p.next: node.next = mapNode[p.next]
            if p.random: node.random = mapNode[p.random]
            p = p.next
        return mapNode[head]
        
        
        '''
         A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

        Return a deep copy of the list.
        '''