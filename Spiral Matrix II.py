'''
Given an integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

For example,
Given n = 3,
You should return the following matrix:

[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]

'''
class Solution:
    # @return a list of lists of integer
    def generateMatrix(self, n):
        x = 1; k = 0
        ret = [[0]*n for j in range(n)]
        while True:
            if n==1:
                ret[0+k][0+k]= x
                return ret
            if n==0:   return ret
            for j in range(n-1):
                ret[0+k][j+k] = x
                x+=1
            for i in range(n-1):
                ret[i+k][n-1+k] = x
                x+=1
            for j in range(n-1, 0, -1):
                ret[n-1+k][j+k] = x
                x+=1
            for i in range(n-1, 0, -1):
                ret[i+k][0+k] = x
                x+=1
            n-=2;     k+=1