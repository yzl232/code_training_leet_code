'''
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

11110
11010
11000
00000

Answer: 1

Example 2:

11000
11000
00100
00011

Answer: 3
'''

# encoding=utf-8
'''
 Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

For example,
Given board =

[
  ["ABCE"],
  ["SFCS"],
  ["ADEE"]
]

'''
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:  return 0
        self.m=m= len(grid); self.n = n= len(grid[0])
        ret = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":       #每次找到一个匹配，就迅速把它替换掉。然后DFS
                    grid[i][j] = '#'
                    ret += 1
                    self.dfs(grid, i, j)
        return ret
    def dfs(self, board, i, j):
        for r, c in  [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
            if 0<=r<self.m and 0<=c<self.n and board[r][c] == "1":
                board[r][c] ='#'
                self.dfs(board, r, c)