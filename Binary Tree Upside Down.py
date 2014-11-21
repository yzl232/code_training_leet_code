# encoding=utf-8
'''
 Given a binary tree where all the right nodes are either leaf nodes with a sibling (a left node that shares the same parent node) or empty, flip it upside down and turn it into a tree where the original right nodes turned into left leaf nodes. Return the new root.
For example:
Given a binary tree {1,2,3,4,5},

    1
   / \
  2   3
 / \
4   5

return the root of the binary tree [4,5,2,#,#,3,1].

   4
  / \
 5   2
    / \
   3   1

confused what "{1,#,2,3}" means?
'''
# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return root of the upside down tree
    def upsideDownBinaryTree(self, root):
        return self.dfs(root, None)

    def dfs(self, p, parent):
        if not p: return parent
        root = self.dfs(p.left, p)
        p.left = parent.right if parent else None
        p.right = parent
        return root
'''
注意观察。
p.left = parent.right;
p.right = parent;  而且它只是弄了左边。。。没弄右边。
1. Recursively traverse to the leftmost node.
2. This becomes the NewRoot, and keep returning this value, up the chain.
3. Make the following changes
'''