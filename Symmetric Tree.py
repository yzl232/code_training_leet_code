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
        return root==None or self.dfs(root.left, root.right)
    
    def dfs(self, l, r):  # not x 在和  and在一起的时候老出问题,原   因不明.
        return (l == r == None) or (l!=None and r!=None and l.val == r.val and self.dfs(l.left, r.right) and self.dfs(l.right, r.left))

'''
from collections import deque
class Solution:
    def isSymmetric(self, root):
        if not root or (not root.left and not root.right): return True
        lq, rq = deque([root.left]), deque([root.right])
        while lq and rq:
            left, right = lq.popleft(), rq.popleft()
            if not left and not right: continue
            if not left or not right or (left.val != right.val) : return False
            lq.append(left.left); lq.append(left.right); rq.append(right.right); rq.append(right.left)
        return True
'''