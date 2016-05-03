'''
Given a binary tree, find the length of the longest consecutive sequence path.

The path refers to any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The longest consecutive path need to be from parent to child (cannot be the reverse).

For example,

   1
    \
     3
    / \
   2   4
        \
         5

Longest consecutive sequence path is 3-4-5, so return 3.

   2
    \
     3
    / 
   2    
  / 
 1

Longest consecutive sequence path is 2-3,not3-2-1, so return 2.
'''

class Solution:
    def longestConsecutive(self, root):
        self.ret = 0
        self.dfs(root, 0, None)
        return self.ret
    
    def dfs(self, root, cnt, pre):
        if not root: return 
        cnt = 1 if root.val != pre else cnt + 1
        self.ret = max(self.ret, cnt)
        self.dfs(root.left, cnt, root.val + 1)
        self.dfs(root.right, cnt, root.val + 1)
        
'''
class Solution:
    def longestConsecutive(self, root):
        if not root:    return 0
        ret = 0;  pre = [(root, 1)]
        while pre:
            cur = []
            for x, cnt in pre:
                ret = max(ret, cnt)
                if x.left:    cur.append((x.left, cnt+1 if x.left.val == x.val + 1 else 1))
                if x.right:   cur.append((x.right, cnt+1 if x.right.val == x.val + 1 else 1))
            pre = cur
        return ret
'''