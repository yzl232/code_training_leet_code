class Solution(object):
    def lengthOfLIS(self, nums):# O(n2)
        tails = [0] * len(nums)
        size = 0
        for x in nums:
            i, j = 0, size
            while i < j:   #我们搜索x。想要更新最小长度x
                m = (i + j) / 2
                if x > tails[m]:     i = m + 1   #x更大，  size肯定比他多1
                else:       j = m      # 寻找需要更新的地方. x是最小的长度为i+1的ending
            tails[i] = x
            size = max(i + 1, size)
        return size
'''
class Solution(object):
    def lengthOfLIS(self, arr):# O(n2)
        """
        :type nums: List[int]
        :rtype: int
        """
        if not arr: return 0
        ret = 1;  n = len(arr)
        dp = [1 for i in range(n)]
        for i in range(1, n):
            dp[i] = max([1+dp[j] for j in range(i) if arr[j]<arr[i]] +[1])
            ret = max(ret, dp[i])
        return ret
'''