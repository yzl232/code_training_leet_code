'''
 Given n balloons, indexed from 0 to n-1. Each balloon is painted with a number on it represented by array nums. You are asked to burst all the balloons. If the you burst balloon i you will get nums[left] * nums[i] * nums[right] coins. Here left and right are adjacent indices of i. After the burst, the left and right then becomes adjacent.

Find the maximum coins you can collect by bursting the balloons wisely.

Note:
(1) You may imagine nums[-1] = nums[n] = 1. They are not real therefore you can not burst them.
(2) 0 ≤ n ≤ 500, 0 ≤ nums[i] ≤ 100

Example:

Given [3, 1, 5, 8]

Return 167

    nums = [3,1,5,8] --> [3,5,8] -->   [3,8]   -->  [8]  --> []
   coins =  3*1*5      +  3*5*8    +  1*3*8      + 1*8*1   = 167

'''

class Solution(object):
    def maxCoins(self, arr):     #正着看, l, i, r相邻.   但是倒着推理, l, i中间可能有爆炸掉了的
        self.d = {}; arr= [1] + arr + [1]   #爆炸只少掉一个.
        return self.dfs(0, len(arr) - 1, arr)

    def dfs(self, l, r, arr):
        if (l, r) not in self.d:
            self.d[(l, r)] = max([arr[l]*arr[i]*arr[r] + self.dfs(l, i, arr) + self.dfs(i, r, arr) for i in range(l + 1, r)] or [0])
        return self.d[(l, r)]

'''
class Solution(object):
    def maxCoins(self, iNums):
        nums = [1] + [i for i in iNums if i > 0] + [1]
        n = len(nums)
        dp = [[0]*n for _ in xrange(n)]

        for k in xrange(2, n):
            for left in xrange(0, n - k):
                right = left + k
                for i in xrange(left + 1,right):
                    dp[left][right] = max(dp[left][right],
                           nums[left] * nums[i] * nums[right] + dp[left][i] + dp[i][right])
        return dp[0][n - 1]
'''