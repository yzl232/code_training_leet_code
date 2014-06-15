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
        if head == None:return None
        cur = head
        while cur: # insert additional nodes
            temp = RandomListNode(cur.label)
            temp.next = cur.next
            cur.next = temp
            cur = temp.next
        cur = head
        while cur: # copy random pointers
            temp = cur.next
            if cur.random: temp.random = cur.random.next
            cur = temp.next
        cur = head
        newHead = head.next
        while cur:  # decouple the list
            temp = cur.next
            cur.next = temp.next
            if temp.next: temp.next = temp.next.next
            cur = cur.next
        return newHead
