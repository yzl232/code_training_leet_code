'''
 Given a collection of numbers that might contain duplicates, return all possible unique permutations.

For example,
[1,1,2] have the following unique permutations:
[1,1,2], [1,2,1], and [2,1,1].
'''

class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def permuteUnique(self, num):
        num.sort()
        self.ret = [];
        self.dfs( [], num)
        return self.ret

    def dfs(self, cur, nums):
        if not nums:
            self.ret.append(cur)
            return
        for i in range(len(nums)):
            if i>0 and nums[i] == nums[i-1]: continue
            t = nums[:]
            self.dfs(cur+[t.pop(i)], t)