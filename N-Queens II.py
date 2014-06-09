class Solution:
    # @return an integer
    def totalNQueens(self, n):
        self.res = 0
        self.solve(n, 0, [-1 for i in range(n)])
        return self.res

    def solve(self, n, currQueenNum, board):
        if currQueenNum == n:
            self.res +=1
            return
        for i in range(n):
            valid = True
            for k in range(currQueenNum):
                if board[k] == i:
                    valid = False
                    break
                if abs(board[k] - i) == abs(currQueenNum - k):
                    valid = False
                    break
            if valid:
                board[currQueenNum] = i
                self.solve(n, currQueenNum+1, board)