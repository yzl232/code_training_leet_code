'''
 Given two binary trees, write a function to check if they are equal or not.

Two binary trees are considered equal if they are structurally identical and the nodes have the same value.
'''
# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param p, a tree node
    # @param q, a tree node
    # @return a boolean
    def isSameTree(self, p, q):  #和symmitric tree题目一模一样
        return (p==q==None) or (p!=None and q!=None and p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right))