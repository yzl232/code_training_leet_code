
'''
Given a binary tree, return the preorder traversal of its nodes' values.

For example:
Given binary tree {1,#,2,3},

   1
    \
     2
    /
   3

return [1,2,3].

Note: Recursive solution is trivial, could you do it iteratively?
'''

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def preorderTraversal(self, root):
        stack = []
        if root: stack.append(root)
        ret = []
        while stack:
            cur = stack.pop()
            ret.append(cur.val)
            if cur.right: stack.append(cur.right)
            if cur.left: stack.append(cur.left)
        return ret
        '''
        # Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def preorderTraversal(self, root):
        self.result = []
        self.dfs(root)
        return self.result

    def dfs(self, root):
        if not root:
            return
        self.result.append(root.val)
        self.dfs(root.left)
        self.dfs(root.right)
        '''