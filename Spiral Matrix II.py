class Solution:
    # @return a list of lists of integer
    def generateMatrix(self, n):
        matrix = [[0 for i in range(n)] for j in range(n)]
        digit = 1; m = n; k = 0 
        while True:
            if n % 2 == 1 and k == (n-1)/2:
                matrix[k][k] = digit
                return matrix
            if digit > n*n:
                return matrix
            for i in range(m-1):
                matrix[0+k][i+k] = digit
                digit+=1
            for i in range(m-1):
                matrix[i+k][m-1+k] = digit
                digit+=1
            for i in range(m-1):
                matrix[m-1+k][m-1-i+k] = digit
                digit +=1
            for i in range(m-1):
                matrix[m-1-i+k][0+k] = digit
                digit+=1
            k +=1
            m-=2