# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def levelOrderBottom(self, root):
        self.results = []
        self.dfs(root, 0)
        return self.results[::-1]
        
    def dfs(self, root, level):
        if not root: return
        if len(self.results) <= level: self.results.append([])
        self.results[level].append(root.val)
        self.dfs(root.left, level+1)
        self.dfs(root.right, level+1)
        
'''
Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree {3,9,20,#,#,15,7},

    3
   / \
  9  20
    /  \
   15   7

return its bottom-up level order traversal as:

[
  [15,7],
  [9,20],
  [3]
]

'''