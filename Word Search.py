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
    def exist(self, board, word):
        self.m, self.n = len(board), len(board[0])
        for i in range(self.m):
            for j in range(self.n):
                if board[i][j] == word[0]:       #每次找到一个匹配，就迅速把它替换掉。然后DFS
                    t, board[i][j] = board[i][j], '#'
                    if self.dfs(board, i, j, word[1:]): return True
                    board[i][j] = t
        return  False

    def dfs(self, board, i, j, word):
        if not word: return True
        for r, c in  [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
            if 0<=r<=self.m-1 and 0<=c<=self.n-1:
                if board[r][c] == word[0]:
                    t, board[r][c] = board[r][c], '#'
                    if self.dfs(board, r, c, word[1:]): return True
                    board[r][c] = t
        return False