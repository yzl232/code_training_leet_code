'''
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

    Integers in each row are sorted in ascending from left to right.
    Integers in each column are sorted in ascending from top to bottom.

For example,

Consider the following matrix:

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]

'''

class Solution(object):
    def searchMatrix(self, matrix, x):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix: return False
        m = len(matrix); n = len(matrix[0])
        i=0;  j=n-1
        while i<m and j>=0:
            if matrix[i][j]==x:   return True
            elif matrix[i][j]>x:    j-=1
            else:   i+=1
        return False