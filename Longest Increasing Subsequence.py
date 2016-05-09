class Solution(object):
    def lengthOfLIS(self, nums):# O(nlogn)
        arr = [0] * len(nums);  ret = 0
        for x in nums:  #tail存的是长度i+1. 的subsequence的尾部元素, val最小的那个.
            l, h = 0, ret   #r=ret比较重要, ret右边是0.   ret = size , 如果size增加, 正好由size-1+1变成size
            while l < h:   #我们搜索x。想要更新最小长度x
                m = (l + h) / 2
                if arr[m] < x:     l = m + 1   #x更大，  size肯定比他多1
                else:  h = m      # 寻找需要更新的地方. x是最小的长度为i+1的ending
            arr[l] = x;  ret = max(l + 1, ret) # tail存的是长度i+1.
        return ret  #通过观察发现， x每次都要update到某个地方的， 要么增加size， 要么减小某个前面的tails[i]
'''
class Solution(object):
    def lengthOfLIS(self, arr):# O(n2)
        """
        :type nums: List[int]
        :rtype: int
        """
        if not arr: return 0
        dp = [1]*len(arr)
        for i in range(1, len(dp)):
            dp[i] = max([dp[j]+1  for j in range(i) if arr[i]>arr[j]] or [1])
        return max(dp)
'''

'''

tails is an array storing the smallest tail of all increasing subsequences with length i+1 in tails[i]. For example, say we have nums = [4,5,6,3], then all the available increasing subsequences are:

len = 1   :      [4], [5], [6], [3]   => tails[0] = 3
len = 2   :      [4, 5], [5, 6]       => tails[1] = 5
len = 3   :      [4, 5, 6]            => tails[2] = 6

We can easily prove that tails is a increasing array. Therefore it is possible to do a binary search in tails array to find the one needs update.

Each time we only do one of the two:

(1) if x is larger than all tails, append it, increase the size by 1
(2) if tails[i-1] < x <= tails[i], update tails[i]

Doing so will maintain the tails invariant. The the final answer is just the size.
'''