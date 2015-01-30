
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
        pre = [root]; rets = [[root.val]]; lvl=1
        while pre:
            cur = []
            for x in pre:
                if x.left: cur.append(x.left)
                if x.right: cur.append(x.right)
            vals = [x.val for x in cur]
            if lvl%2==1: vals.reverse()
            if vals: rets.append(vals)
            pre = cur; lvl+=1
        return rets
'''
class Solution:
    def zigzagLevelOrder(self, root):
        if not root: return []
        prev, ret, lvl = [root], [], 1
        while prev:
            cur, vals = [], []
            for n in prev:
                vals.append(n.val)
                if n.left:  cur.append(n.left)
                if n.right:  cur.append(n.right)
            if lvl%2==0:  ret.append(vals[::-1])
            else: ret.append(vals)
            prev = cur;  lvl+=1
        return ret


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