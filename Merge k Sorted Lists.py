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
    def mergeKLists(self, arr):
        h = [(x.val, x) for x in arr if x]
        heapq.heapify(h)
        dummy = ListNode(0); cur = dummy
        while h:
            val, x = heapq.heappop(h)
            cur.next = x;  cur = cur.next;
            if x.next: heapq.heappush(h, (x.next.val, x.next))
        return dummy.next