'''
Given n, how many structurally unique BST's (binary search trees) that store values 1...n?

For example,
Given n = 3, there are a total of 5 unique BST's.

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3


'''
class Solution:
    # @return an integer
    def numTrees(self, n):
        dp = [1 for i in range(n+1)]
        for i in range(1, n+1):
            dp[i] = sum(dp[j]*dp[i-1-j] for j in range(i))
        return dp[-1]
# number in the left child tree(0~ i-1).  number in the right child tree. 左边的数目是0~n-1  . 因为root总有一个。右边i-l-1个
#http://fisherlei.blogspot.com/2013/03/leetcode-unique-binary-search-trees.html