'''
Given a 2D matrix matrix, find the sum of the elements inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).

Range Sum Query 2D
The above rectangle (with the red border) is defined by (row1, col1) = (2, 1) and (row2, col2) = (4, 3), which contains sum = 8.

Example:

Given matrix = [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]

sumRegion(2, 1, 4, 3) -> 8
update(3, 2, 2)
sumRegion(2, 1, 4, 3) -> 10

Note:

    The matrix is only modifiable by the update function.
    You may assume the number of calls to update and sumRegion function is distributed evenly.
    You may assume that row1 ≤ row2 and col1 ≤ col2.

'''

class NumMatrix(object):  # Right
    def __init__(self, grid):
        if not grid:  return
        self.m, self.n = len(grid), len(grid[0])
        self.grid, self.bit = [[0] * (self.n) for i in xrange(self.m)], [[0] * (self.n + 1) for i in xrange(self.m + 1)]
        for i in range(self.m):
            for j in range(self.n):
                self.update(i, j, grid[i][j])

    def update(self, r, c, val):
        diff, self.grid[r][c], i = val - self.grid[r][c], val, r + 1
        while i < self.m+1:
            j = c+1   #每个循环都要重新set
            while j < self.n+1:
                self.bit[i][j] += diff
                j += (j & -j)
            i += (i & -i)

    def sumRegion(self, r1, c1, r2, c2):
        return self.getSum(r2, c2) + self.getSum(r1 - 1, c1 - 1) - self.getSum(r1 - 1, c2) - self.getSum(r2, c1 - 1)

    def getSum(self, r, c):
        ret, i = 0, r+1
        while i>0:
            j = c+1
            while j>0:
                ret += self.bit[i][j]
                j -= (j & -j)
            i -= (i & -i)
        return ret

# Your NumMatrix object will be instantiated and called as such:
# numMatrix = NumMatrix(matrix)
# numMatrix.sumRegion(0, 1, 2, 3)
# numMatrix.update(1, 1, 10)
# numMatrix.sumRegion(1, 2, 3, 4)