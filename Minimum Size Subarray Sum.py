'''
 Given an array of n positive integers and a positive integer s, find the minimal length of a subarray of which the sum ≥ s. If there isn't one, return 0 instead.

For example, given the array [2,3,1,2,4,3] and s = 7,
the subarray [4,3] has the minimal length under the problem constraint.

click to show more practice.
More practice:

If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log n).

'''
#和谷歌那道著名的cumulative的sum array挺像的。
#区别：  这个是正数， 大于等于， 用双指针。滑动窗口。  那个是等于， 可以是负数

class Solution:
    # @param {integer} s
    # @param {integer[]} nums
    # @return {integer}
    def minSubArrayLen(self, target, arr):
        ret = len(arr)+10
        s = 0;  l=0
        for r in range(len(arr)):
            s+=arr[r]
            if s>=target:
                while s-arr[l]>=target:
                    s-=arr[l];  l+=1
                ret = min(r-l+1, ret)
        if ret==len(arr)+10: return 0
        return ret