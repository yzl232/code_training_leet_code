# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def reverseList(self, h):
        if not h or not h.next: return h
        h2 = self.reverseList(h.next)
        h.next.next, h.next =h, None
        return h2
#  1=>2=>3=>4
#      1=>2=>3<=4   return 4
#     1=>2<=3<=4  return 4
#     1<=2<=3<=4

'''
class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def reverseList(self, head):
        return self.dfs(head, None)

    def dfs(self, h, newH):
        if not h:   return newH
        x = h.next;   h.next = newH
        return self.dfs(x, h)


class Solution(object):
    def reverseList(self, h):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not h: return
        dummy= ListNode(0); dummy.next=  h
        pre, last, cur = dummy, h, h.next
        while cur:  #last一直是最后一个。 不变。
            last.next = cur.next
            cur.next = pre.next
            pre.next = cur
            cur = last.next   #四层的封闭连环
        return dummy.next
'''
# 每次把cur搬运过来， 到pre后面。 连接pre, pre.next中间
# dummy作为pre。
# 虽然不难。 但是过段时间就忘。 不算容易。
#不需要pre了. dummy就是pre.