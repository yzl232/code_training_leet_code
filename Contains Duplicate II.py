'''
Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the difference between i and j is at most k. 
'''

class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {boolean}
    def containsNearbyDuplicate(self, nums, k):
        d = {} #像two sum， 是按顺序拍好的i, 天生递增。 
        for i, x in enumerate(nums):
            if x in d and i-d[x]<=k: return True
            d[x] = i
        return False