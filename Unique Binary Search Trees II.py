'''
Given n, generate all structurally unique BST's (binary search trees) that store values 1...n.

For example,
Given n = 3, your program should return all 5 unique BST's shown below.

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3


'''

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @return a list of tree node
    def generateTrees(self, n):
        return self.dfs(1, n) if n>0 else []

    def dfs(self, l, h):
        if l>h: return [None]
        ret = []
        for rootV in range(l, h+1):
            for i in self.dfs(l, rootV-1):
                for j in self.dfs(rootV+1, h):
                    x = TreeNode(rootV)
                    x.left ,x.right = i, j
                    ret.append(x)
        return ret
'''  #稍微改一下Treenode定义， 可以变成2行的答案。
class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

class Solution:
    # @return a list of tree node
    def generateTrees(self, n):
        return self.dfs(1, n)

    def dfs(self, l, h):
        if l>h: return [None]
        return [TreeNode(rootV, x, y) for rootV in range(l, h+1) for x in self.dfs(l, rootV-1) for y in self.dfs(rootV+1, h)]


'''