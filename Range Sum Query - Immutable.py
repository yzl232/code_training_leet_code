'''
Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

Example:

Given nums = [-2, 0, 3, -5, 2, -1]

sumRange(0, 2) -> 1
sumRange(2, 5) -> -1
sumRange(0, 5) -> -3

Note:

    You may assume that the array does not change.
    There are many calls to sumRange function.

'''
class NumMatrix(object):
      def __init__(self, matrix):
          if not matrix:  return
          n, m = len(matrix), len(matrix[0])
          self.s = [[0 for j in xrange(m + 1)] for i in xrange(n + 1)]
          for i in xrange(1, n+1):
              for j in xrange(1, m+1):
                  self.s[i][j] = matrix[i - 1][j - 1] + self.s[i][j - 1] + self.s[i - 1][j] - self.s[i - 1][j - 1]


      def sumRegion(self, r1, c1, r2, c2):
          return self.s[r2+1][c2+1] - self.s[r2+1][c1 ] - self.s[r1][c2+1] + self.s[r1 ][c1 ]  #这一行非得举例子才能写清楚。

 