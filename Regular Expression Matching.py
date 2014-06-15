class Solution:
    # @param s, an input string
    # @param p, a pattern string       
    # @return a boolean
    def isMatch(self, s, p):
        if len(s)>0 and len(p)>0 and p[-1] != '*' and p[-1] != '.' and p[-1] != s[-1]: return False
        #http://blog.csdn.net/lifajun90/article/details/10582733
        #different from https://oj.leetcode.com/problems/wildcard-matching/. Since '*' has different meaning here
        #http://www.programcreek.com/2012/12/leetcode-regular-expression-matching-in-java/
        if len(p) == 0:
            return len(s) == 0
        if len(p) == 1 or p[1] !='*':   #if next char is '*', that's a different case
            if len(s) == 0 :
                return False
            if p[0] != '.' and p[0] != s[0]:
                return False
            return self.isMatch(s[1:], p[1:])
        else:    # len(p)>=2 and p[1] == '*'
            l1 = len(s)
            i = -1
            while i<l1 and (i<0 or p[0] == '.' or p[0] == s[i]):
                if (self.isMatch(s[i+1:], p[2:])):   #Try each condition
                    return True
                i+=1
            return False