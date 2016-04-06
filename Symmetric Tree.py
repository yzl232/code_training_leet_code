# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isSymmetric(self, root):  #和same tree一模一样.  dfs的自变量都是放入left和right。
        if not root: return True
        return self.dfs(root.left, root.right)
    
    def dfs(self, left, right):
        if not left and not right:return True
        if not left or not right: return False
        if left.val != right.val: return False
        return self.dfs(left.left, right.right) and self.dfs(left.right, right.left)
'''

#snap面经有iterative的
from collections import deque
class Solution:
    def isSymmetric(self, root):
        if not root or (not root.left and not root.right): return True
        lq = deque([root.left])
        rq = deque([root.right])
        while lq and rq:
            left, right = lq.popleft(), rq.popleft()
            if not left and not right: continue
            if not left or not right: return False
            if left.val != right.val : return False
            lq.append(left.left)
            lq.append(left.right)
            rq.append(right.right)
            rq.append(right.left)
        return True
'''