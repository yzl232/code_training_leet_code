'''
 The thief has found himself a new place for his thievery again. There is only one entrance to this area, called the "root." Besides the root, each house has one and only one parent house. After a tour, the smart thief realized that "all houses in this place forms a binary tree". It will automatically contact the police if two directly-linked houses were broken into on the same night.

Determine the maximum amount of money the thief can rob tonight without alerting the police.

Example 1:

     3
    / \
   2   3
    \   \ 
     3   1

Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.

Example 2:

     3
    / \
   4   5
  / \   \ 
 1   3   1

Maximum amount of money the thief can rob = 4 + 5 = 9. 
'''


class Solution(object):
    def rob(self, root):
        def dfs(x):
            if not x: return (0, 0)
            l, r = dfs(x.left), dfs(x.right)
            return (l[1] + r[1], max(l[1] + r[1], l[0] + r[0] + x.val))
        return dfs(root)[1]

        
'''
noRoot(node) = curMax(node.left) + curMax(node.right) 

curMax(node) = max( noRoot(node.left)+noRoot(node.right)+node.value, noRoot(node) ).


class Solution(object):
    def rob(self, root):
        def dfs(x):
            if not x: return (0, 0)
            l, r = dfs(x.left), dfs(x.right)
            return (l[1] + r[1], max(l[1] + r[1], l[0] + r[0] + x.val))
        return dfs(root)[1]

        

noRoot(node) = curMax(node.left) + curMax(node.right) 

curMax(node) = max( noRoot(node.left)+noRoot(node.right)+node.value, noRoot(node) ).

#有点像这道题。 geeks: Given a Binary Tree, find size of the Largest Independent Set(LIS)

'''