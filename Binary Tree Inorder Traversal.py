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
        result = []
        cur = root
        while True:
            while cur:
                stack.append(cur)
                cur = cur.left
            if len(stack) == 0: break
            else:
                cur = stack.pop()
                result.append(cur.val)
                cur = cur.right
        return result

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
    def inorderTraversal(self, root):
        self.result = []
        self.dfs(root)
        return self.result

    def dfs(self, root):
        if not root:
            return

        self.dfs(root.left)
        self.result.append(root.val)
        self.dfs(root.right)
'''