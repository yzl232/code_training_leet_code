# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isSymmetric(self, root):
        if not root: return True
        return self.check(root.left, root.right)

    def check(self, left, right):
        if not left and not right: return  True
        if not left or not right: return False
        if left.val != right.val: return False
        return self.check(left.left, right.right) and self.check(left.right, right.left)