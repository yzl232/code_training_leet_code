'''
Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the difference between i and j is at most k. 
'''
class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {boolean}
    def containsNearbyDuplicate(self, nums, k):
        d = {} #像two sum， 是按顺序拍好的i, 天生递增。 
        for i in range(len(nums)):
            if nums[i] in d and i - d[nums[i]] <= k:   return True
            d[nums[i]] = i
        return False