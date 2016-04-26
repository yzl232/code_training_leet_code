# encoding=utf-8
'''
Write a program to find the node at which the intersection of two singly linked lists begins.

For example, the following two linked lists:

A:          a1 → a2
                   ↘
                     c1 → c2 → c3
                   ↗
B:     b1 → b2 → b3

begin to intersect at node c1.


Notes:

    If the two linked lists have no intersection at all, return null.
    The linked lists must retain their original structure after the function returns.
    You may assume there are no cycles anywhere in the entire linked structure.
    Your code should preferably run in O(n) time and use only O(1) memory.

'''

class Solution:
    # @param two ListNodes
    # @return the intersected ListNode
    def getIntersectionNode(self, h1, h2):
        l1, l2 = self.getCnt(h1), self.getCnt(h2)
        if l1<l2:  h2, h1 = h1, h2
        for i in range(abs(l1-l2)):    h1 = h1.next
        while h1 and h2:
            if h1==h2: return h1
            h1, h2 = h1.next, h2.next

    def getCnt(self, h):
        cnt = 0
        while h:
            h= h.next
            cnt+=1
        return cnt

# 第1种方法更快。 第2种更加简洁。  第二种很难写。 第一种很好写。
'''
class Solution:
    # @param two ListNodes
    # @return the intersected ListNode
    def getIntersectionNode(self, h1, h2):
        p1=h1;  p2 =h2
        if not p1 or not p2: return
        while p1 and p2 and p1!=p2:
            p1=p1.next;  p2=p2.next
            if p1==p2: return p1
            if not p1: p1=h2
            if not p2: p2=h1
        return p1

#  l1, l2.     l1>l2:        l2+(l1-x),   l1+(l2-x)
# 如果没有相交。 第二次会同时到达null。
'''