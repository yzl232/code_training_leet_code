# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def inorderTraversal(self, root):
        stack = []
        n = root
        result = []
        while True:
            while n:
                stack.append(n)
                n = n.left
            if len(stack) == 0: break
            else:
                n = stack.pop()
                result.append(n.val)
                n = n.right
        return result
        
        '''
        Given a binary tree, return the inorder traversal of its nodes' values.

        For example:
        Given binary tree {1,#,2,3},

           1
            \
             2
            /
           3

        return [1,3,2].

        Note: Recursive solution is trivial, could you do it iteratively?
        
        '''