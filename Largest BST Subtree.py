'''
Given a binary tree, find the largest subtree which is a Binary Search Tree (BST), where largest means subtree with largest number of nodes in it.

Note:
A subtree must include all of its descendants.
Here's an example:

    10
    / \
   5  15
  / \   \ 
 1   8   7

The Largest BST Subtree in this case is the highlighted one.
The return value is the subtree's size, which is 3.

Hint:

    You can recursively use algorithm similar to 98. Validate Binary Search Tree at each node of the tree, which will result in O(nlogn) time complexity.

Follow up:
Can you figure out ways to solve it with O(n) time complexity? 

'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):  #min, max用来验证BST.  
    def largestBSTSubtree(self, root):
        self.ret = 0
        self.dfs(root)
        return self.ret

    def dfs(self, root):
        if not root: return (0, float('inf'), float('-inf')) #注意反了， 这是为了应对root没有child的情况   max1 < root.val <min2
        (n1, min1, max1), (n2, min2, max2)= self.dfs(root.left), self.dfs(root.right)
        n = n1+1+n2 if max1 < root.val <min2 else float('-inf')
        self.ret = max(self.ret, n)
        return n, min(min1, root.val), max(max2, root.val)
#本来要加一个isBST变量.  用了float('-inf')就不用了

'''
class Solution(object):  #min, max用来验证BST.  
    def largestBSTSubtree(self, root):
        def dfs(root):
            if not root: return (0, 0, float('inf'), float('-inf'))
            (x1, n1, min1, max1), (x2, n2, min2, max2)= dfs(root.left), dfs(root.right)
            n = n1+1+n2 if max1 < root.val < min2 else float('-inf')
            return (max(x1, x2, n), n, min(min1, root.val), max(max2, root.val))
        return dfs(root)[0]

'''