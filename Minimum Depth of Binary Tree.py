'''
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
'''

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#实质上是最浅的叶子。

class Solution:
    # @param root, a tree node
    # @return an integer
    def minDepth(self, root):
        if not root: return 0
        pre = [root]; lvl=1   # 除了pre, cur之外
        while pre:
            cur = []     #必须用array。 因为是有序的。 并且不会有重复
            for n in pre:
                if n.left:  cur.append(n.left)
                if n.right:  cur.append(n.right)
                if not n.left and not n.right: return lvl
            pre = cur; lvl+=1

'''
class Solution:
    # @param root, a tree node
    # @return an integer
    def minDepth(self, root):
        if not root: return 0
        MAX_INT = 10**10
        self.ret = MAX_INT
        self.dfs(root, 1)
        return self.ret

    def dfs(self, root, lvl):
        if not root: return
        if not root.left and not root.right:   self.ret = min(self.ret, lvl)
        self.dfs(root.left, lvl+1)
        self.dfs(root.right, lvl+1)

#class variable


class Solution:
    # @param root, a tree node
    # @return an integer
    def minDepth(self, root):
        if not root: return 0
        if not root.left and not root.right: return 1
        if not root.left:  return 1+self.minDepth(root.right)
        if not root.right: return 1+self.minDepth(root.left)
        return min(self.minDepth(root.left), self.minDepth(root.right))+1


If the root has two branches, where the left one has depth 1,  and the right one has depth 100000, this solution will still have to go down the longest branch.

Level-by-level traversal would find min depth faster.
'''