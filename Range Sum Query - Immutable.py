'''
Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

Example:

Given nums = [-2, 0, 3, -5, 2, -1]

sumRange(0, 2) -> 1
sumRange(2, 5) -> -1
sumRange(0, 5) -> -3

Note:

    You may assume that the array does not change.
    There are many calls to sumRange function.

'''
class NumArray(object):
    def __init__(self, nums):
        self.accu = [0]  #考虑为0的时候,  acumu多放一个0比较合适. 
        for x in nums:    self.accu.append(self.accu[-1] + x)

    def sumRange(self, i, j):
        return self.accu[j + 1] - self.accu[i]

 