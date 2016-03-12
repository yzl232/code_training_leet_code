
'''
 Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

For example,
Given 1->2->3->3->4->4->5, return 1->2->5.
Given 1->1->1->2->3, return 2->3. 

'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):     #当head可能被删除, 不知道第一个node是哪个。 一般就用dummy。 retuen dummy.next
        if not head or not head.next: return head
        dummy = ListNode(0)
        cur, dummy.next = dummy, head
        while cur.next:
            pre = cur.next
            while pre.next and pre.next.val == pre.val:     pre = pre.next
            if pre!=cur.next:   cur.next = pre.next   #有移动的，要删除.  并且可能要连续删掉，所以不移动p。
            else:  cur=cur.next  #没有移动的，不用删除。
        return dummy.next