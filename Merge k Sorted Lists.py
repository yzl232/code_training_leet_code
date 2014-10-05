# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param a list of ListNode
    # @return a ListNode
    def mergeKLists(self, lists):
        if len(lists) ==0 : return None
        while len(lists)>1:
            newlists = []
            for i in range(0, len(lists)-1, 2):
                newlists.append(self.mergeTwoLists(lists[i], lists[i+1]))
            if len(lists)%2==1: newlists.append(lists[-1])
            lists = newlists
        return lists[0]
            
    def mergeTwoLists(self, l1, l2):
        dummy = ListNode(0)
        prev = dummy
        while l1 and l2:
            if l1.val > l2.val:
                prev.next = l2
                l2=l2.next
            else:
                prev.next = l1
                l1 = l1.next
            prev = prev.next
        if l1:prev.next = l1
        elif l2:prev.next = l2
        return dummy.next