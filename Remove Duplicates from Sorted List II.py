# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        if not head or not head.next: return head
        dummy = ListNode(-10*10)
        dummy.next = head
        p = dummy
        while p.next:
            p2 = p.next
            while p2.next and p2.next.val == p2.val:
                p2 = p2.next 
            if p2!=p.next:    
                p.next = p2.next   #in this case, we start over and do not change p pointer
            else:   p = p.next     
        return dummy.next
'''
 Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

For example,
Given 1->2->3->3->4->4->5, return 1->2->5.
Given 1->1->1->2->3, return 2->3. 

'''