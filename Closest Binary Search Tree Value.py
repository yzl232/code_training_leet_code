'''


    Given a non-empty binary search tree and a target value, find the value in the BST that is closest to the target.

    Note: Given target value is a floating point. You are guaranteed to have only one unique value in the BST that is closest to the target.

'''

#做过。
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
class Solution:
    def closestValue(self, root, target):
        a = root.val
        kid = root.left if target < a else root.right
        if not kid: return a
        b = self.closestValue(kid, target)
        return min((b, a), key=lambda x: abs(target - x))
'''