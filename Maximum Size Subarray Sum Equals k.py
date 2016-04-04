'''
 Given an array nums and a target value k, find the maximum length of a subarray that sums to k. If there isn't one, return 0 instead.

Example 1:

Given nums = [1, -1, 5, -2, 3], k = 3,
return 4. (because the subarray [1, -1, 5, -2] sums to 3 and is the longest)

Example 2:

Given nums = [-2, -1, 2, 1], k = 1,
return 2. (because the subarray [-1, 2] sums to 1 and is the longest)

Follow Up:
Can you do it in O(n) time? 
'''

class Solution(object):  #以前的accuMulate的是return是否。 这个是最大。
    def maxSubArrayLen(self, nums, k):
        ans, acc = 0, 0               # answer and the accumulative value of nums
        d = {0:-1}                 #key is acc value, and value is the index
        for i in xrange(len(nums)):
            acc += nums[i]
            if acc not in d:  d[acc] = i 
            if acc-k in d:    ans = max(ans, i-d[acc-k])
        return ans