class Solution:
    # @param s, an input string
    # @param p, a pattern string       
    # @return a boolean
    def isMatch(self, s, p):
        if len(s)>=1 and len(p)>=1 and s[-1] != p[-1] and p[-1] != '.' and p[-1] != '*': return False
        if len(p) == 0: return len(s) ==0
        if len(p)==1 or p[1] != '*':#if next char is '*', that's a different case
            if len(s)==0 or (s[0]!=p[0] and p[0]!='.'): return False
            return self.isMatch(s[1:], p[1:])
        else: # len(p)>=2 and p[1] == '*'
            i = -1
            while i< len(s) and (i<0 or s[i] == p[0] or p[0]=='.'):
                i+=1
                if self.isMatch(s[i:], p[2:]): return True
            return False
        #http://blog.csdn.net/lifajun90/article/details/10582733
        #different from https://oj.leetcode.com/problems/wildcard-matching/. Since '*' has different meaning here
        #http://www.programcreek.com/2012/12/leetcode-regular-expression-matching-in-java/
