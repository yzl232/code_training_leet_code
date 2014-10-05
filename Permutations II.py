class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def permuteUnique(self, num):
        num.sort()
        self.result = []; 
        self.dfs( [], num)
        return self.result
        
    def dfs(self, tmpResult, nums):
        if len(nums) == 0 and tmpResult not in self.result:
            self.result.append(tmpResult)
            return
        else:
            for i in range(len(nums)):
                if i>0 and nums[i] == nums[i-1]: continue
                tmpNums = nums[:]
                self.dfs(tmpResult+[tmpNums.pop(i)], tmpNums)