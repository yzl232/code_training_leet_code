'''
 Given a 2D board and a list of words from the dictionary, find all words in the board.

Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

For example,
Given words = ["oath","pea","eat","rain"] and board =

[
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]

Return ["eat","oath"].

Note:
You may assume that all inputs are consist of lowercase letters a-z.

click to show hint.

You would need to optimize your backtracking to pass the larger test. Could you stop backtracking earlier?

If the current candidate does not exist in all words' prefix, you could stop backtracking immediately. What kind of data structure could answer such query efficiently? Does a hash table work? Why or why not? How about a Trie? If you would like to learn how to implement a basic trie, please work on this problem: Implement Trie (Prefix Tree) first.


'''

class Solution:
    # @param {character[][]} board
    # @param {string[]} words
    # @return {string[]}
    def findWords(self, board, words):
        if not board or not words: return []
        trie=self.buildTrie(words); self.ret=set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.dfs(board,i,j,trie, "")
        return list(self.ret)

    def dfs(self, board, i, j, trie, cur):
        if board[i][j] not in trie: return
        trie = trie[board[i][j]]; cur+=board[i][j]
        if "#" in trie:   self.ret.add(cur)
        t, board[i][j] = board[i][j], '$'
        for r, c in  [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:  
            if 0<=r<len(board) and 0<=c<len(board[0]): self.dfs(board, r, c, trie, cur)
        board[i][j] = t
        
    def buildTrie(self, words):
        trie={}
        for w in words:
            cur=trie
            for ch in w:
                if ch not in cur:   cur[ch]={}
                cur=cur[ch]
            cur['#']='#'
        return trie