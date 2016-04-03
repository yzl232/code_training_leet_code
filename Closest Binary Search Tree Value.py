'''


    Given a non-empty binary search tree and a target value, find the value in the BST that is closest to the target.

    Note: Given target value is a floating point. You are guaranteed to have only one unique value in the BST that is closest to the target.

'''

#做过。
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def closestValue(self, root, x):
        if not root: return 
        ret = root.val;  cur = root
        while cur:
            if abs(cur.val - x)<abs(ret-x): ret = cur.val
            cur = cur.right if cur.val<x else cur.left
        return int(ret)
'''
class Solution:
    def findPreSuc(self, root, x):
        self.x = x; self.ret = root
        self.dfs(root)
        return self.ret

    def dfs(self, root):
        if not root: return
        if abs(root.val-self.x)<abs(self.ret-self.x): self.ret = root.val
        if root.val == self.x:      return
        elif root.val>self.x:     self.dfs(root.left)
        else:   self.dfs(root.right)
'''



'''
class Solution:
    def closestValue(self, root, target):
        a = root.val
        kid = root.left if target < a else root.right
        if not kid: return a
        b = self.closestValue(kid, target)
        return min((b, a), key=lambda x: abs(target - x))
'''