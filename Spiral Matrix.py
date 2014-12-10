'''
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

For example,
Given the following matrix:

[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]

You should return [1,2,3,6,9,8,7,4,5].
'''
class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of integers
    def spiralOrder(self, matrix):
        if not matrix: return []
        m, n, k = len(matrix), len(matrix[0]), 0
        ret = []
        while True:
            if m==0 or n ==0 : return ret
            if m==1:
                for i in range(n):   ret.append(matrix[0+k][i+k])
                return ret
            if n==1:
                for i in range(m):    ret.append(matrix[i+k][ 0+k])  #两两对称。可以加速写
                return ret
            for i in range(n-1):    ret.append(matrix[0+k][i+k])       #注意到四个的两两对称，可以检查和加速写
            for i in range(m-1):    ret.append(matrix[i+k][n-1+k])
            for i in range(n-1, 0, -1):    ret.append(matrix[m-1+k][i+k])
            for i in range(m-1, 0, -1):     ret.append(matrix[i+k][0+k])
            k+=1;   n-=2;    m-=2