# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None
#based on level order traversal
class Solution:
    # @param root, a tree node
    # @return nothing
    def connect(self, root):
        self.result = []
        self.dfs(root, 1)
        for nodes in self.result:
            l = len(nodes)
            for i in range(l-1):
                nodes[i].next = nodes[i+1]
        
    def dfs(self, root, level):
        if not root: return
        if len(self.result)< level: self.result.append([])
        self.result[level-1].append(root)
        self.dfs(root.left, level+1)
        self.dfs(root.right, level+1)