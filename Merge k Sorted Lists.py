'''
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param a list of ListNode
    # @return a ListNode
    def mergeKLists(self, lists):
        temp = []
        for n in lists:
            while n:
                temp.append((n.val, n))
                n = n.next
        temp.sort()
        dummy = ListNode(-1)
        pre = dummy
        for i in range(len(temp)):
            node = temp[i][1]
            pre.next = node
            pre = pre.next
        pre.next =None
        return dummy.next
        '''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param a list of ListNode
    # @return a ListNode
    def mergeKLists(self, nodes):
        if len(nodes) ==0 : return None
        while len(nodes)>1:
            newLists = []
            for i in range(0, len(nodes)-1, 2):
                newLists.append(self.mergeTwoLists(nodes[i], nodes[i+1]))
            if len(nodes)%2==1: newLists.append(nodes[-1])
            nodes = newLists
        return nodes[0]
        
        
            
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
        '''