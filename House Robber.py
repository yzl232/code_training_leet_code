'''
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

Credits:
Special thanks to @ifanchu for adding this problem and creating all test cases. Also thanks to @ts for adding additional test cases.
'''
class Solution:
    # @param num, a list of integer
    # @return an integer
    def rob(self, num):
        size = len(num)
        odd, even = 0, 0
        for i in range(size):
            if i % 2:
                odd = max(odd + num[i], even)
            else:
                even = max(even + num[i], odd)
        return max(odd, even)
'''
class Solution:
    # @param num, a list of integer
    # @return an integer
    def rob(self, num):
        n = len(num)
        dp = [0] * (n + 1)
        if n:   dp[1] = num[0]
        for i in range(2, n + 1):
            dp[i] = max(dp[i - 1], dp[i - 2] + num[i - 1])   #转移方程有点像maxmum subarray.
        return dp[-1]
'''