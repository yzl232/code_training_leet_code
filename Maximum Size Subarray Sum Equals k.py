'''
 Given an array nums and a target value k, find the maximum length of a subarray that sums to k. If there isn't one, return 0 instead.

Example 1:

Given nums = [1, -1, 5, -2, 3], k = 3,
return 4. (because the subarray [1, -1, 5, -2] sums to 3 and is the longest)

Example 2:

Given nums = [-2, -1, 2, 1], k = 1,
return 2. (because the subarray [-1, 2] sums to 1 and is the longest)

Follow Up:
Can you do it in O(n) time? 
'''

class Solution(object):  #以前的accuMulate的是return是否。 这个是最大。
    def maxSubArrayLen(self, arr, k):
        ret, cur, d = 0, 0, {0:-1}               # answer and the accumulative value of nums
        for i in xrange(len(arr)):
            cur += arr[i]
            if cur not in d:  d[cur] = i  #求maximum要限定条件更新hashtable。  minimum随时更新。
            if cur-k in d:    ret = max(ret, i-d[cur-k])
        return ret
    #与sliding window区别在于 acumu是等于。   sliding window是大于等于