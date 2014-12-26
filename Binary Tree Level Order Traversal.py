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
        pre, ret = [root], []   # 除了pre, cur之外，还用了第三个vals
        while pre:
            cur, vals = [], []     #必须用array。 因为是有序的。 并且不会有重复
            for n in pre:
                vals.append(n.val)
                if n.left:  cur.append(n.left)
                if n.right:  cur.append(n.right)
            ret.append(vals)
            pre = cur
        return ret
'''
BFS的做法和DFS的做法

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def levelOrder(self, root):
        self.ret = []
        self.dfs(root, 1)
        return self.ret

    def dfs(self, root, lvl):
        if not root: return
        if len(self.ret) < lvl: self.ret.append([]) #   否则下面append不了的。 要加上
        self.ret[lvl-1].append(root.val) #因为这里level马上要用到。
        self.dfs(root.left, lvl+1)
        self.dfs(root.right, lvl+1)

'''