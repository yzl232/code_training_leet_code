# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a list node
    # @return a tree node
    def sortedListToBST(self, head):
        array = []
        p = head
        while p:
            array.append(p.val)
            p = p.next
        return self.createBST(array, 0, len(array) - 1)

    def createBST(self, num, start, end):
        if start > end:return None
        mid = (start + end)/2
        root = TreeNode(num[mid])
        root.left = self.createBST(num, start, mid-1)
        root.right = self.createBST(num, mid+1, end)
        return root
        
        #Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.

