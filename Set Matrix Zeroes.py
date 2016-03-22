#Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in place.
class Solution:
    # @param matrix, a list of lists of integers
    # RETURN NOTHING, MODIFY matrix IN PLACE.
    def setZeroes(self, mtx):
        if not mtx: return []
        row0=col0=False;  m=len(mtx); n=len(mtx[0])
        for i in range(m):
            if mtx[i][0] == 0:  col0= True
        for j in range(n):
            if mtx[0][j] == 0:  row0= True
        for i in range(1, m):
            for j in range(1, n): #利用第一行，第一列标记
                if mtx[i][j]==0:  mtx[i][0] = mtx[0][j] = 0
        for i in range(1, m):
            for j in range(1, n):
                if mtx[i][0] ==0 or mtx[0][j]==0:  mtx[i][j] = 0
        for i in range(m):
            if col0: mtx[i][0] = 0
        for j in range(n):
            if row0: mtx[0][j] = 0

# 第一行的corner case也成立。 如果本身为0，当然0.
# 如果本身不是0，看mtx[0][0]标记
'''
class Solution:
    # @param matrix, a list of lists of integers
    # RETURN NOTHING, MODIFY matrix IN PLACE.
    def setZeroes(self, matrix):
        if matrix == []:    return
        row =set([]); col = set([])
        m = len(matrix);    n = len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    row.add(i);   col.add(j)
        for i in range(m):
            for j in range(n):
                if i in row or j in col:    matrix[i][j] = 0
'''