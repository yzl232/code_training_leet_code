'''
Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

    For example, given array S = {-1 2 1 -4}, and target = 1.

    The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

'''
class Solution:
    # @return an integer
    def threeSumClosest(self, num, target):
        num.sort();     ret = ( 0, 10**10)
        for i in range(len(num)):
            l = i+1;     r = len(num) - 1
            if i>0 and num[i] == num[i-1]: continue
            while l<r:
                s = num[i] + num[l] + num[r]
                diff = abs(target-s)
                if diff<ret[-1]: ret=(s, diff)
                if s == target:     return  target
                elif s<target:     l+=1
                else:  r -=1
        return ret[0]