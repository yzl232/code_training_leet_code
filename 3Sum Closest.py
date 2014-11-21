'''
Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

    For example, given array S = {-1 2 1 -4}, and target = 1.

    The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

'''

class Solution:
    # @return an integer
    def threeSumClosest(self, num, target):
        num.sort()
        minDiff = 10**10
        ret = 0
        for i in range(len(num)):
            left = i+1
            right = len(num) - 1
            if i>0 and num[i] == num[i-1]: continue
            while left<right:
                s = num[i] + num[left] + num[right]
                diff = abs(target-s)
                if diff<minDiff:
                    minDiff = diff
                    ret = s
                if s == target:
                    return  target
                elif s<target:
                    left+=1
                else:
                    right -=1
        return ret