
'''

 Given a collection of integers that might contain duplicates, S, return all possible subsets.

Note:

    Elements in a subset must be in non-descending order.
    The solution set must not contain duplicate subsets.

For example,
If S = [1,2,2], a solution is:

[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]

'''

class Solution:
    # @param num, a list of integer
    # @return a list of lists of integer
    def subsetsWithDup(self, s):
        ret = [[]];  s.sort()
        for i in s:
            ret +=[ j+[i] for j in ret if j+[i] not in ret]
        return ret
'''

class Solution:
    # @param S, a list of integer
    # @return a list of lists of integer
    def subsetsWithDup(self, nums):
        nums.sort()
        self.result = []
        self.dfs([], nums)
        return self.result

    def dfs(self, cur, nums):
        self.result.append(cur)
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]: continue
            self.dfs(cur + [nums[i]], nums[i + 1:])
        
class Solution:
    # @param S, a list of integer
    # @return a list of lists of integer
    def subsetsWithDup(self, nums):
        self.nums = sorted(nums)
        self.ret = []
        self.dfs([], 0)
        return self.ret

    def dfs(self, cur, st):
        self.ret.append(cur)
        for i in range(st, len(self.nums)):
            if i>st and self.nums[i]==self.nums[i-1]: continue
            self.dfs(cur + [self.nums[i]], i+1)

'''