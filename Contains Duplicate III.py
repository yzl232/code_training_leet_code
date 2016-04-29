'''
Given an array of integers, find out whether there are two distinct indices i and j in the array such that the difference between nums[i] and nums[j] is at most t and the difference between i and j is at most k. 
'''

class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @param {integer} t
    # @return {boolean}
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        if t < 0: return False
        d = {};   w = t + 1
        for i, x in enumerate(nums):
            if any(y in d and abs(x-d[y])<w  for y in [x/w - 1, x/w, x/w+1]): return True
            d[x/w] = x
            if i >= k: del d[nums[i - k] / w]
        return False