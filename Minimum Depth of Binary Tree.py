# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def minDepth(self, root):
        if not root: return 0
        elif root.left == None and root.right == None:
            return 1
        elif root.left == None:
            return 1+self.minDepth(root.right)
        elif root.right == None:
            return 1+self.minDepth(root.left)
        else:
            return min(self.minDepth(root.left), self.minDepth(root.right))+1
            
        '''
        Given a binary tree, find its minimum depth.

        The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
        '''