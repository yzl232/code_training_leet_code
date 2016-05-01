'''
Given a binary tree, count the number of uni-value subtrees.

A Uni-value subtree means all nodes of the subtree have the same value.

For example:
Given binary tree,

              5
             / \
            1   5
           / \   \
          5   5   5

return 4. 
'''
class Solution:
    def countUnivalSubtrees(self, root):
        self.cnt = 0
        self.dfs(root)
        return self.cnt

    def dfs(self, root):
        if not root:   return True
        l, r = self.dfs(root.left), self.dfs(root.right)
        if l and r and all(not x or x.val==root.val for x in (root.left, root.right)):
            self.cnt += 1
            return True
        return False

    # bottom-up, first check the leaf nodes and count them,
    # then go up, if both children are "True" and root.val is
    # equal to both children's values if exist, then root node
    # is uniValue suntree node.
#尝试这么做：  if self.dfs(root.left) and self.dfs(root.right) and all
#错了。  因为如果左边为False， 会跳过right。 right也必须跑， 这里计算cnt， 和一般的题目不一样。
'''
class Solution:
    def countUnivalSubtrees(self, root):
        self.cnt = 0
        self.dfs(root)
        return self.cnt

    def dfs(self, root):
        if not root:   return True
        l, r = self.dfs(root.left), self.dfs(root.right)
        if l and r and (not root.left or root.left.val == root.val) and (not root.right or root.right.val == root.val):
            self.cnt += 1
            return True
        return False
'''
    # bottom-up, first check the leaf nodes and count them,
    # then go up, if both children are "True" and root.val is
    # equal to both children's values if exist, then root node
    # is uniValue suntree node.