class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def permute(self, num):
        n = len(num)
        self.results = []
        self.dfs(num, 0, n)
        return self.results

    def dfs(self, num, l, h):
        if l>h: return
        for i in range(l, h):
            a = num[:]
            a[i], a[l] = a[l], a[i]
            if a not in self.results: self.results.append(a)
            self.dfs(a, l+1, h)