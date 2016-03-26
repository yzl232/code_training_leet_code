class Solution:
    # @param {character[][]} board
    # @param {string[]} words
    # @return {string[]}
    def findWords(self, board, words):
        if not board or not words: return []
        trie={};         self.ret=set()
        for w in words:
            cur=trie
            for ch in w:
                if ch not in cur:   cur[ch]={}
                cur=cur[ch]
            cur['#']='#'
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.dfs(board,i,j,trie, "")
        return list(self.ret)

    def dfs(self, board, i, j, trie, word):
        if board[i][j] not in trie: return
        trie = trie[board[i][j]]; word+=board[i][j]
        if "#" in trie:   self.ret.add(word)
        t, board[i][j] = board[i][j], '$'
        for r, c in  [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
            if 0<=r<len(board) and 0<=c<len(board[0]): self.dfs(board, r, c, trie, word)
        board[i][j] = t
