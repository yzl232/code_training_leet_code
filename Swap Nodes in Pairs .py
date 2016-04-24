# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 递归的code更简洁. 不过有stack space
class Solution:
    # @param a ListNode
    # @return a ListNode
    def swapPairs(self, h):
        if not h or not h.next: return h
        n = h.next
        h.next = self.swapPairs(n.next)   #再次形成类似环的双斜杠.
        n.next = h
        return n



'''
class Solution:
    # @param a ListNode
    # @return a ListNode   #顺序  pre,  last, cur
    def swapPairs(self, h):  
        dummy = ListNode(0)
        pre, dummy.next, one = dummy, h, h
        while one and one.next:  #考虑操纵2个node.这是必须的。
            two = one.next
            one.next = two.next
            two.next = pre.next
            pre.next = two
            #以上连环
            pre = one       #与reverse linkedlist 区别。  不断更新pre, last
            one = one.next  #普通的逆转，pre和last不会变的。。
        return dummy.next


'''