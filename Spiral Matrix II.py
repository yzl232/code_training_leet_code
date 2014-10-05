class Solution:
    # @return a list of lists of integer
    def generateMatrix(self, n):
        digit = 1
        result = [[0 for i in range(n)] for j in range(n)]
        k = 0
        while True:
            if n==1:
                result[0+k][0+k]= digit
                return result
            if n==0:
                return result
            for i in range(n-1):
                result[0+k][i+k] = digit
                digit+=1
            for i in range(n-1):
                result[i+k][n-1+k] = digit
                digit+=1
            for i in range(n-1):
                result[n-1+k][n-1-i+k] = digit
                digit+=1
            for i in range(n-1):
                result[n-1-i+k][0+k] = digit
                digit+=1
            n-=2
            k+=1