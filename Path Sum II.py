# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a list of lists of integers
    def pathSum(self, root, sum):
        self.result = []
        self.dfs(root, sum, [])
        return self.result
    
    def dfs(self, root, sum, cur):
        if not root: return
        if not root.left and not root.right and sum == root.val:
            self.result.append(cur + [root.val])
            return
        self.dfs(root.left, sum-root.val, cur+[root.val])
        self.dfs(root.right, sum-root.val, cur+[root.val])
        
        
        '''
         Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.
        For example:
        Given the below binary tree and sum = 22,

                      5
                     / \
                    4   8
                   /   / \
                  11  13  4
                 /  \    / \
                7    2  5   1

        return

        [
           [5,4,11,2],
           [5,8,4,5]
        ]
        
        
        '''