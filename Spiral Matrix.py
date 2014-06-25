class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of integers
    def spiralOrder(self, matrix):
        if matrix == []: return []
        m = len(matrix); n = len(matrix[0]); k = 0
        self.results = []
        self.collectSpiralOrder(matrix, m, n, 0)
        return self.results

    def collectSpiralOrder(self, matrix, m, n, k):
        if m == 1:
            for i in range(n):
                self.results.append(matrix[0+k][i+k])
            return self.results
        if n == 1:
            for i in range(m):
                self.results.append(matrix[i+k][0+k])
            return self.results
        for i in range(n-1):
            self.results.append(matrix[0+k][i+k])
        for i in range(m-1):
            self.results.append(matrix[i+k][k+n-1])
        for i in range(n-1):
            self.results.append(matrix[k+m-1][n-1-i+k])
        for i in range(m-1):
            self.results.append(matrix[m-1-i+k][0+k])
        if m >= 3 and n>=3:
            self.collectSpiralOrder(matrix, m-2, n-2, k+1)