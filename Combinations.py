'''
 Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

For example,
If n = 4 and k = 2, a solution is:

[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]

'''

class Solution:
    # @return a list of lists of integers
    def combine(self, n, k):
        self.n, self.k, self.ret = n, k, []
        self.dfs(1, [])
        return self.ret

    def dfs(self, start, cur ):
        if len(cur) == self.k:
            self.ret.append(cur)
            return
        for i in range(start, self.n+1):
            self.dfs(i+1,  cur+[i])# i+1,  which  means only add the number that is bigger (nums[i+1:]) .  In permutations, we choose all the other numbers except this i.  tempNums.pop()

#复杂度是O( choose k from n) = O(c(n, k))