'''
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3

But the following is not:

    1
   / \
  2   2
   \   \
   3    3

Note:
Bonus points if you could solve it both recursively and iteratively.
'''
# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isSymmetric(self, root):  #和same tree一模一样
        if not root: return True
        return self.dfs(root.left, root.right)

    def dfs(self, l, r):
        if not l and not r:return True
        if not l or not r: return False
        if l.val != r.val: return False
        return self.dfs(l.left, r.right) and self.dfs(l.right, r.left)