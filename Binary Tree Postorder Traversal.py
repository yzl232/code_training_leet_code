# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def postorderTraversal(self, root):
        if not root: return []
        stack = []
        results = []
        stack.append(root)
        while len(stack) > 0:
            cur = stack.pop()
            results.append(cur.val)
            if cur.left: stack.append(cur.left)
            if cur.right: stack.append(cur.right)
        return results[::-1]
        
        
        '''
        Given a binary tree, return the postorder traversal of its nodes' values.

        For example:
        Given binary tree {1,#,2,3},

           1
            \
             2
            /
           3

        return [3,2,1].

        Note: Recursive solution is trivial, could you do it iteratively?
        
        
        '''
        
        
        
# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution1:
    # @param root, a tree node
    # @return a list of integers
    def postorderTraversal(self, root):
        self.result = []
        self.dfs(root)
        return self.result
    
    def dfs(self, root):
        if not root:
            return
        self.dfs(root.left)
        self.dfs(root.right)
        self.result.append(root.val)
        