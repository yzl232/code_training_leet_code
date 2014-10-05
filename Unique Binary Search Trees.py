class Solution:
    # @return an integer
    def numTrees(self, n):
        dp = [0 for i in range(n+1)]   # include when there are 0 elements
        dp[0] = 1
        for i in range(1, n+1):
            for leftNum in range(i):
                dp[i]+= dp[leftNum]*dp[i-1-leftNum]
        return dp[n]
        
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