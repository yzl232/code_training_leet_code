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
    def isPalindrome(self, head):  #  考虑了1->2->3. 发现没有问题
        if not head: return True
        fast = slow = head
        # find the mid node
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        # reverse the second half
        dummy = ListNode(0); dummy.next = slow;
        pre = dummy; last = slow; cur = slow.next
        while cur:
            last.next = cur.next
            cur.next = pre.next
            pre.next = cur
            cur = last.next
        node = dummy.next
        # compare the first and second half nodes
        while node: # while node and head:
            if node.val != head.val:
                return False
            node = node.next
            head = head.next
        return True