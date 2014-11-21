'''
Implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
isMatch("aa","a") → false
isMatch("aa","aa") → true
isMatch("aaa","aa") → false
isMatch("aa", "a*") → true
isMatch("aa", ".*") → true
isMatch("ab", ".*") → true
isMatch("aab", "c*a*b") → true
'''

class Solution:
    # @return a boolean
    def isMatch(self, s, p):
        if len(s)>=1 and len(p)>=1 and s[-1] != p[-1] and p[-1] != '.' and p[-1] != '*': return False
        dp=[[False for i in range(len(p)+1)] for j in range(len(s)+1)]
        dp[0][0]=True
        for i in range(1,len(p)+1):
            if p[i-1]=='*':  #dp[i], p本身就是i-1。2个字符以前的。  1个字符以前靠不住。
                if i>=2:
                    dp[0][i]=dp[0][i-2] #s 为空时。      ****是匹配的  1*
        for i in range(1,len(s)+1):
            for j in range(1,len(p)+1):
                if p[j-1]=='.':
                    dp[i][j]=dp[i-1][j-1]
                elif p[j-1]=='*':#dp[i][j-1]一次。 dp[i][j-2]   0次。   i-1对应*号。s:      aa   对应 p:  a*
                    dp[i][j]=dp[i][j-1] or dp[i][j-2] or (dp[i-1][j] and (s[i-1]==p[j-2] or p[j-2]=='.'))
                else:
                    dp[i][j]=dp[i-1][j-1] and s[i-1]==p[j-1]
        return dp[len(s)][len(p)]


'''
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
'''