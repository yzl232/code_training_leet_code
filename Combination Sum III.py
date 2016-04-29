'''


Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.

Ensure that numbers within the set are sorted in ascending order.

Example 1:

Input: k = 3, n = 7

Output:

[[1,2,4]]


Example 2:

Input: k = 3, n = 9

Output:

[[1,2,6], [1,3,5], [2,3,4]]

'''

class Solution:
    # @param {integer} k
    # @param {integer} n
    # @return {integer[][]}
    def combinationSum3(self, k, target):
        self.ret = [];  self.k = k
        self.dfs(target, 1, [] )
        return self.ret

    def dfs(self, target, start,cur ):
        if target<0: return
        if len(cur)==self.k:
            if target==0:   self.ret.append(cur)
            return
        for x in range(start, 10):   self.dfs(target-x, x+1, cur+[x])   #x+1有点容易写错写成start+1