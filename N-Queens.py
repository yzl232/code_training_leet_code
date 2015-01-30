'''
Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space respectively.

For example,
There exist two distinct solutions to the 4-queens puzzle:

[
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]

'''



class Solution:
    # @return a list of lists of string
    def solveNQueens(self, n):
        self.rets = []; self.n = n
        self.dfs( [],  0)
        return self.rets

    def dfs(self, cur, rowN):
        if rowN == self.n:
            self.rets.append(['.' * c + "Q" + '.' * (self.n - c - 1) for c in cur])
            return
        for c in range(self.n):
            if c not in cur and True not in [abs(rowN - r) == abs(c - cur[r]) for r in  range(len(cur)) ]:
                self.dfs(cur + [c],  rowN + 1)          #row行, 第i列。  j行。cur[j]列


'''
class Solution:    # a little similar to Sudoku question
    # @return a list of lists of string   # since each line set once, we only need to check each column and each diagnoal
    def solveNQueens(self, n):
        self.result = []    # the one-dimension array stores the information where the queen locates
        self.solve(n, 0, [-1 for i in range(n)] )# because array is easier to manipulate
        return  self.result
    def solve(self, n, currQueenNum, board):
        if currQueenNum == n:  # recursion ends, prepare the answer
            oneAnswer = [['.' for j in range(n)] for i in range(n)]
            for i in range(n):
                oneAnswer[i][board[i]] = 'Q'
                oneAnswer[i] = ''.join(oneAnswer[i])
            self.result.append(oneAnswer)
            return
#Use a int vector to store the current state,  A[i]=j refers that the ith row and jth column is placed a queen
        for i in range(n):  # try every column
            valid = True
            for k in range(currQueenNum):  #  as I think, in range(n) is also fine  
                #chech column
                if board[k] == i:
                    valid = False
                    break
                if abs(board[k] - i) == abs(currQueenNum - k):
                    valid = False
                    break
            if valid:
                board[currQueenNum] = i
                self.solve(n, currQueenNum + 1, board)
'''