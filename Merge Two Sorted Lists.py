#Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.
class Solution:
    # @param two ListNodes
    # @return a ListNode
    def mergeTwoLists(self, l1, l2):
        dummy = pre = ListNode(-1)
        while l1 and l2:   #用了pre。  也用了dummy
            if l1.val > l2.val:
                pre.next = l2
                l2 = l2.next
            else:
                pre.next = l1
                l1 = l1.next
            pre = pre.next
        pre.next = l1 or l2
        return dummy.next

'''
class Solution:
    # @param two ListNodes
    # @return a ListNode
    def mergeTwoLists(self, l1, l2):
        if (not l1) or (not l2): return l1 or l2
        if l1.val<l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2
'''