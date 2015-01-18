'''
 Given a collection of numbers, return all possible permutations.

For example,
[1,2,3] have the following permutations:
[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], and [3,2,1].
'''

class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def permute(self, num):
        self.ret = []; num.sort()
        self.dfs( [], num)
        return self.ret
        
    def dfs(self, cur, nums):
        if not nums:
            self.ret.append(cur)
            return
        for i in range(len(nums)):
            t = nums[:]
            self.dfs(cur+[t.pop(i)], t)
# 注意说复杂度是O(n!)。 因为有n!个结果