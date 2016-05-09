'''
Follow up for N-Queens problem.

Now, instead outputting board configurations, return the total number of distinct solutions.
'''

class Solution:
    # @return an integer
    def totalNQueens(self, n):
        self.ret = 0; self.n = n
        self.dfs( [],  0)
        return self.ret

    def dfs(self, cur, r):
        if r == self.n:
            self.ret+=1
            return
        for c in range(self.n):
            if c not in cur and all(abs(r - r1) != abs(c - c1) for r1, c1 in enumerate(cur)):  self.dfs(cur + [c], r + 1) 
#row行, 第i列。  j行。cur[j]列


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
'''