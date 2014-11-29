'''
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree {3,9,20,#,#,15,7},

    3
   / \
  9  20
    /  \
   15   7

return its level order traversal as:

[
  [3],
  [9,20],
  [15,7]
]

'''
# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root):
        if not root: return []
        prev, res = [root], []
        while prev:
            cur, vals = [], []
            for node in prev:
                vals.append(node.val)
                if node.left:  cur.append(node.left)
                if node.right:  cur.append(node.right)
            res.append(vals)
            prev = cur
        return res
'''

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def levelOrder(self, root):
        self.result = []
        self.dfs(root, 0)
        return self.result

    def dfs(self, root, level):
        if not root: return
        if len(self.result) <= level: self.result.append([]) #   否则下面append不了的。 要加上
        self.result[level].append(root.val) #因为这里level马上要用到。
        self.dfs(root.left, level+1)
        self.dfs(root.right, level+1)
'''