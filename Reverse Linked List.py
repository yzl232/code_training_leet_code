# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def reverseList(self, head):
        return self.doReverse(head, None)
    def doReverse(self, h, newH):
        if not h:
            return newH
        next = h.next
        h.next = newH
        return self.doReverse(next, h)
        '''
class Solution(object):
    def reverseList(self, h):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not h: return
        dummy= ListNode(0); dummy.next=  h
        last, cur = h, h.next
        while cur:  #last一直是最后一个。 不变。
            last.next = cur.next
            cur.next = dummy.next
            dummy.next = cur
            cur = last.next   #四层的封闭连环
        return dummy.next
'''
# 每次把cur搬运过来， 到pre后面。 连接pre, pre.next中间
# dummy作为pre。
# 虽然不难。 但是过段时间就忘。 不算容易。
#不需要pre了. dummy就是pre.