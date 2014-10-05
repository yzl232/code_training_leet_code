class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of integers
    def spiralOrder(self, matrix):
        if matrix == []:  return []
        m = len(matrix); n = len(matrix[0]); k = 0  
        results = []
        while True:
            if m==0 or n == 0: return results
            if (m == 1):
                for i in range(n):
                    results.append(matrix[k][i+k])
                return results
            if (n == 1):
                for i in range(m):
                    results.append(matrix[i+k][k])
                return results
            for i in range(n-1):
                results.append(matrix[k][i+k])
            for i in range(m-1):
                results.append(matrix[i+k][k+n-1])
            for i in range(n-1):
                results.append(matrix[k+m-1][k+n-1-i])
            for i in range(m-1):
                results.append(matrix[k+m-1-i][k])
            m-=2
            n-=2
            k+=1