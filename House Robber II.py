'''
After robbing those houses on that street, the thief has found himself a new place for his thievery so that he will not get too much attention. This time, all houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, the security system for these houses remain the same as for those in the previous street.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.'''

class Solution:  #取了0, 就不能取最后一个,  取了最后一个, 不能取0
    # @param {integer[]} nums
    # @return {integer}#注意区分一下geeks的circular subarray
    def rob(self, nums):  #circular导致多了0, n-1这一对相邻
        return nums[0] if len(nums) == 1 else max(self.robLinear(nums[1:]), self.robLinear(nums[:-1]))

    # @param num, a list of integer
    # @return an integer
    def robLinear(self, nums):
        ppre, pre = 0, 0
        for x in nums:   ppre, pre = pre, max(ppre + x, pre)
        return pre