'''
Follow up for N-Queens problem.

Now, instead outputting board configurations, return the total number of distinct solutions.
'''

class Solution:
    # @return an integer
    def totalNQueens(self, n):
        self.result = 0
        self.n = n
        self.dfs(0, [-1 for i in range(n)])
        return self.result
    
    def dfs(self, curNum, board):
        if curNum == self.n:
            self.result +=1
            return 
        else:
            for i in range(self.n):
                valid = True
                for k in range(curNum):
                    if i == board[k]:
                        valid = False
                        break
                    if abs(i-board[k]) == abs(k - curNum):
                        valid = False
                        break
                if valid:
                    board[curNum] = i
                    self.dfs(curNum+1, board)
        