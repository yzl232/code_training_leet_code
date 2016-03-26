'''
After robbing those houses on that street, the thief has found himself a new place for his thievery so that he will not get too much attention. This time, all houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, the security system for these houses remain the same as for those in the previous street.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.'''

class Solution:
    # @param {integer[]} nums
    # @return {integer}#注意区分一下geeks的circular subarray
    def rob(self, nums):
        if len(nums) == 1:
            return nums[0]
        return max(self.robLinear(nums[1:]), self.robLinear(nums[:-1]))
        
    # @param num, a list of integer
    # @return an integer
    def robLinear(self, num):
        size = len(num)
        odd, even = 0, 0
        for i in range(size):
            if i % 2:
                odd = max(odd + num[i], even)
            else:
                even = max(even + num[i], odd)
        return max(odd, even)
