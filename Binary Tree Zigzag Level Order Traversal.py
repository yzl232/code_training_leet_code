'''
Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree {3,9,20,#,#,15,7},

    3
   / \
  9  20
    /  \
   15   7

return its zigzag level order traversal as:

[
  [3],
  [20,9],
  [15,7]
]

confused what "{1,#,2,3}" means? > read more on how binary tree is serialized on OJ.

'''
# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def zigzagLevelOrder(self, root):
        if not root: return []
        prev, res, level = [root], [], 0
        while prev:
            cur, vals = [], []
            for node in prev:
                vals.append(node.val)
                if node.left:  cur.append(node.left)
                if node.right:  cur.append(node.right)
            if level%2:  res.append(vals[::-1])
            else: res.append(vals)
            prev = cur;  level+=1
        return res
'''

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def zigzagLevelOrder(self, root):
        self.result = []
        self.dfs(root, 1)
        for i in range(len(self.result)):
            if i % 2 ==0: continue
            else: self.result[i] =  self.result[i][::-1]
        return self.result

    def dfs(self, root, level):
        if not root: return
        if len(self.result) < level:  self.result.append([])
        self.result[level-1].append(root.val)
        self.dfs(root.left, level+1)
        self.dfs(root.right, level+1)

'''