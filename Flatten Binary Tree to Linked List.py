# encoding=utf-8
'''
 Given a binary tree, flatten it to a linked list in-place.

For example,
Given

         1
        / \
       2   5
      / \   \
     3   4   6

The flattened tree should look like:

   1
    \
     2
      \
       3
        \
         4
          \
           5
            \
             6

'''

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node  #注意这道题目不是binary search tree  。  是类似heap
    # @return nothing, do it in place  #他的顺序是   pre-Order的顺序。    root, left, right.
    def flatten(self, root):  #我们反过来，就是right, left, root
        self.pre = None
        self.dfs(root)

    def dfs(self, root):
        if not root: return
        self.dfs(root.right) #总共三步。 背下
        self.dfs(root.left)
        root.right = self.pre  #右边连上
        self.pre = root    #pre
        root.left = None  #左置空
'''
假如是binary search tree的形式，应当是：  right,  root, left


class Solution:
    # @param root, a tree node
    # @return nothing, do it in place
    def flatten(self, root):
        self.head = None
        self.dfs(root)

    def dfs(self, root):
        if not root: return
        self.dfs(root.right)
        root.right = self.head  #右边连上
        root.left = None  #左置空
        self.head = root    #更新head
        self.dfs(root.left)



# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return nothing, do it in place
    def flatten(self, root):
        if not root: return
        left = root.left
        right = root.right

        if left:
            root.right = left
            root.left = None
            rightMost = left
            while rightMost.right:
                rightMost = rightMost.right
            rightMost.right = right
        self.flatten(root.right)

flatten:     每次处理一个节点。 然后recursion
每次有三步：
1       左节点制空 root.left = None
2 root.right= left
3   rightMost.right = right
'''