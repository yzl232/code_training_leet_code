# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return nothing, do it in place
    def flatten(self, root):
        if not root: return
        left = root.left
        right = root.right
        if left:
            root.right = left
            root.left = None
            rightMost = left
            while rightMost.right:
                rightMost = rightMost.right
            rightMost.right = right
        self.flatten(root.right)