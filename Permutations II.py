class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def permuteUnique(self, num):
        n = len(num)
        self.results = []
        self.dfs(num, 0, n)
        return self.results
    
    def dfs(self, num, k, n):
        if k>n: return
        for i in range(k, n):
            if self.noswap(k, i, num):
                continue
            a = num[:]
            a[i], a[k] = a[k], a[i]
            if a not in self.results: self.results.append(a)
            self.dfs(a, k+1, n)
            
    def noswap(self, k, i, num):
        for j in range(k, i):
            if num[j] == num[i]:
                return True
        return  False