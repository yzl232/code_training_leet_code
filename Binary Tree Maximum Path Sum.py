'''
 Given a binary tree, find the maximum path sum.

The path may start and end at any node in the tree.

For example:
Given the below binary tree,

       1
      / \
     2   3

Return 6.
'''


# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def maxPathSum(self, root):
        self.maxSum = -10**10
        self.dfs(root)
        return self.maxSum

    def dfs(self, root):
        if not root: return 0
        vLeft = self.dfs(root.left)
        vRight = self.dfs(root.right)
        self.maxSum = max(self.maxSum, vLeft+vRight+root.val)
        return max(root.val+vLeft, root.val+vRight, 0)  #pass value up   # since (vLeft+vRight+root.val) can not be passed up,  it is updated before return..       since vLeft, vRight >=0, we do not need to add a single root.val here