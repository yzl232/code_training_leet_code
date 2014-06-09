# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isValidBST(self, root):
        return self.dfs(root, -10**10, 10**100)
    def dfs(self, root, low, high):
        if root == None: return True
        if root.val >= high or root.val <= low:
            return False
        return self.dfs(root.left, low, root.val) and self.dfs(root.right, root.val, high)