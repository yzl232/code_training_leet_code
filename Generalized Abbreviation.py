'''
Write a function to generate the generalized abbreviations of a word.

Example:

Given word = "word", return the following list (order does not matter):

["word", "1ord", "w1rd", "wo1d", "wor1", "2rd", "w2d", "wo2", "1o1d", "1or1", "w1r1", "1o2", "2r1", "3d", "w3", "4"]


如果能想到每一个字符都有2种可能性: abbr或没有abbr.
以"abc"举例: 有3个letter, 所以是$$2^3 = 8$$.
'''

class Solution(object):
    def generateAbbreviations(self, s):
        self.ret = []
        self.dfs("", 0, s)
        return self.ret
    
    def dfs(self, cur, cnt, s):
        if not s:
            self.ret.append(cur+(str(cnt) if cnt>0 else ""))
            return
        self.dfs(cur, cnt + 1, s[1:])
        self.dfs(cur + (str(cnt) if cnt > 0 else "") + s[0], 0, s[1:])  #注意这里加上s[0] . 与完成的还是不同
##a
# return ['a', '1']
##aa
# return ["1a", "a1", "2", "aa"]