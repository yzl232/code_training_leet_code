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
    def maxPathSum(self, root):   # post-order
        self.ret = float('-inf')
        self.dfs(root)
        return self.ret

    def dfs(self, root):
        if not root: return 0
        vL, vR = self.dfs(root.left), self.dfs(root.right)
        self.ret = max(self.ret, vL+vR+root.val)
        return max(root.val+vL, root.val+vR, 0)  #pass value up   # since (vL+vR+root.val) can not be passed up,  it is updated before return..       since vL, vR >=0, we do not need to add a single root.val here