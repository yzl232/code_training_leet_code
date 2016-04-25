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
            l, r = lq.popleft(), rq.popleft()
            if not l and not r: continue    #None也会append。 保证了lq， rq length相等
            if not l or not r or (l.val != r.val) : return False
            lq.append(l.left);  rq.append(r.right)
            lq.append(l.right);  rq.append(r.left)
        return True
'''