'''
Given a singly linked list, determine if it is a palindrome.

Follow up:
Could you do it in O(n) time and O(1) space?
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, h1):
        if not h1: return True
        fast = slow = h1
        # find the mid node
        while fast and fast.next:
            fast, slow = fast.next.next, slow.next
        # reverse the second half
        dummy = ListNode(0); dummy.next = slow;
        pre = dummy; last = slow; cur = slow.next
        while cur:
            last.next = cur.next
            cur.next = pre.next
            pre.next = cur
            cur = last.next
        h2 = dummy.next
        # compare the first and second half nodes
        while h2: # while node and head:
            if h2.val != h1.val:  return False
            h1, h2 = h1.next, h2.next
        return True