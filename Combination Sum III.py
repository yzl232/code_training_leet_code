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
    def combinationSum3(self, k, n):
        self.ret = []
        self.n, self.k = n, k
        self.dfs(0, 0,   1, [] )
        return self.ret

    def dfs(self, cnt, s, start,cur ):
        if s>self.n: return
        if cnt==self.k:
            if s == self.n:   self.ret.append(cur)
            return
        for x in range(start, 10):
            self.dfs(cnt+1, s+x, x+1, cur+[x])
