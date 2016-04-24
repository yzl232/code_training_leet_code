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


class Solution:
    # @param board, a list of lists of 1 length string
    # @param word, a string
    # @return a boolean
    def exist(self, grid, word):
        if not grid or not word: raise ValueError()
        return  any(self.dfs(grid, i, j, word) for i in range(len(grid)) for j in range(len(grid[0])))

    def dfs(self, grid, i, j, word):
        if grid[i][j]== word: return True
        if grid[i][j] != word[0]:  return False     #每次找到一个匹配，就迅速把它替换掉。然后DFS
        t, grid[i][j] = grid[i][j], '#'
        for r, c in  [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
            if 0<=r<len(grid) and 0<=c<len(grid[0]) and self.dfs(grid, r, c, word[1:]): return True
        grid[i][j] = t
        return False

'''
class Solution:
    # @param board, a list of lists of 1 length string
    # @param word, a string
    # @return a boolean
    def exist(self, grid, word):
        if not grid or not word: raise ValueError()
        return  any(self.dfs(grid, i, j, word) for i in range(len(grid)) for j in range(len(grid[0])))

    def dfs(self, grid, i, j, word):
        if not word: return True
        if not (0<=i<len(grid) and 0<=j<len(grid[0]) and grid[i][j] == word[0]):  return False     #每次找到一个匹配，就迅速把它替换掉。然后DFS
        t, grid[i][j] = grid[i][j], '#'
        for r, c in  [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
            if self.dfs(grid, r, c, word[1:]): return True
        grid[i][j] = t
        return False
'''