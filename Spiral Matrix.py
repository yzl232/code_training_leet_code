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
            if m==1:    return ret+[matrix[0+k][i+k] for i in range(n)]
            if n==1:   return ret + [matrix[i+k][ 0+k] for i in range(m)]   #两两对称。可以加速写
            for j in range(n-1):    ret.append(matrix[0+k][j+k])       #注意到四个的两两对称，可以检查和加速写     #i，n  第2维度
            for i in range(m-1):    ret.append(matrix[i+k][n-1+k])  #i, m 第1维度
            for j in range(n-1, 0, -1):    ret.append(matrix[m-1+k][j+k])   #总有一边是变化的，为i+k。 其他的就好办了
            for i in range(m-1, 0, -1):     ret.append(matrix[i+k][0+k])
            k+=1;   n-=2;    m-=2  #先写好这行。 容易忘