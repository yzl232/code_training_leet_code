'''
You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @return a ListNode
    def addTwoNumbers(self, l1, l2):
        carry = 0; head = ListNode(0); curr = head
        while l1 and l2:
            sum = l1.val + l2.val + carry
            carry = sum/10
            curr.next = ListNode(sum%10)
            l1 = l1.next; l2 = l2.next; curr = curr.next
        while l1:
            sum = l1.val+ carry
            carry = sum/10
            curr.next = ListNode(sum%10)
            curr = curr.next; l1 = l1.next
        while l2:
            sum = l2.val + carry
            carry = sum/10
            curr.next = ListNode(sum%10)
            curr = curr.next; l2 = l2.next
        if carry:
            curr.next = ListNode(1)
        return head.next