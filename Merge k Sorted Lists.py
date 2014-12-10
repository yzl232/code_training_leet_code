'''
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.
'''
import heapq

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # @param a list of ListNode
    # @return a ListNode
    def mergeKLists(self, lists):
        h = [(n.val, n) for n in lists if n]
        heapq.heapify(h)
        dummy = ListNode(0); curr = dummy
        while h:
            pop = heapq.heappop(h)
            curr.next = ListNode(pop[0])
            curr = curr.next; n = pop[1].next
            if n:  heapq.heappush(h, (n.val, n))
        return dummy.next