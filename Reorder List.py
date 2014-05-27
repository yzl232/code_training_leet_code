# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#http://www.programcreek.com/2013/12/in-place-reorder-a-singly-linked-list-in-java/
class Solution:
    # @param head, a ListNode
    # @return nothing
    def reorderList(self, head):
        if head == None or head.next == None: return
        # find middle node
        fast = slow = head
        while (fast and fast.next and fast.next.next):
            fast = fast.next.next
            slow = slow.next
        # split
        head2 = slow.next; slow.next = None
        #reverse the second half list
        prev, curr = head2, head2.next
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        head2.next = None
        head2 = prev
        # join the first half and the second half
        p1 = head
        p2 = head2  # short one 
        while(p2):
            temp1 = p1.next
            temp2 = p2.next

            p1.next = p2
            p2.next = temp1

            p1 = temp1
            p2 = temp2
