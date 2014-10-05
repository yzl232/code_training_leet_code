class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def permute(self, num):
        self.result = []; 
        self.dfs( [], num)
        return self.result
        
    def dfs(self, tmpResult, nums):
        if len(nums) == 0 and tmpResult not in self.result:
            self.result.append(tmpResult)
            return
        else:
            for i in range(len(nums)):
                tmpNums = nums[:]
                self.dfs(tmpResult+[tmpNums.pop(i)], tmpNums)