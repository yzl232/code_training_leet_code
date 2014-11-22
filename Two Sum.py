# encoding=utf-8
'''
Given an array of integers, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.

You may assume that each input would have exactly one solution.

Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2
'''
class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        d = {}
        for i in range(len(num)):
            if target - num[i] in d: return (d[target - num[i]]+1, i+1)
            else: d[num[i]] = i


'''
假如是sorted , 那么用two  pointer可以做到O(1) space

class Solution3:
    def twoSum(self, num, target):
        i=0;  j=len(num)-1
        while i<j:
            cur = num[i]+num[j]
            if cur == target: return num[i], num[j]
            elif cur > target:  j-=1
            else: i+=1
num = [1, 3, 5, 8, 13]
s = Solution3()
print s.twoSum(num, 16)
'''