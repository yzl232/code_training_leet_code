'''
Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

    For example, given array S = {-1 2 1 -4}, and target = 1.

    The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

'''
class Solution:
    # @return an integer
    def threeSumClosest(self, arr, target):
        arr.sort();     ret = (float('inf'), None)
        for i in range(len(arr)):
            if i>0 and arr[i] == arr[i-1]: continue
            l = i+1;     r = len(arr) - 1
            while l<r:
                s = arr[i] + arr[l] + arr[r]
                ret = min(ret, (abs(s-target), s))
                if s == target:     return  target
                elif s<target:     l+=1
                else:  r -=1
        return ret[1]