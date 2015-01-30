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
    # @param s, an input string
    # @param p, a pattern string
    # @return a boolean
    def isMatch(self, s, p):
        if s and p and p[-1] not in (s[-1], '*', '.'): return False  #这一行是为了通过leetcode.  其实要删掉
        return self.dfs(s, p)

    def dfs(self, s, p):
        if not p: return not s
        if len(p)>=2 and p[1]=='*':
             if self.dfs(s, p[2:]): return True
             if s and p[0] in ('.', s[0]) and self.dfs(s[1:], p): return True
             return False
        return s!='' and p[0] in ('.', s[0]) and self.dfs(s[1:], p[1:])   #和上面某行一样。    这样子就不容易出错。


        #http://blog.csdn.net/lifajun90/article/details/10582733
        #different from https://oj.leetcode.com/problems/wildcard-matching/. Since '*' has different meaning here
#http://www.programcreek.com/2012/12/leetcode-regular-expression-matching-in-java/


'''
class Solution:  #和递归其实没有区别。  一个思路
    # @return a boolean
    def isMatch(self, s, p):
        if s and p and p[-1] not in (s[-1], '*', '.'): return False  #这一行是为了通过leetcode.  其实要删掉
        dp=[[False for i in range(len(p)+1)] for j in range(len(s)+1)]
        dp[0][0]=True
        for j in range(2,len(p)+1):  #dp[i], p本身就是i-1。2个字符以前的。  1个字符以前靠不住。
            if p[j-1]=='*':    dp[0][j]=dp[0][j-2] #s 为空时。p不能使单独星号。 可以使******没问题
        for i in range(1,len(s)+1):
            for j in range(1,len(p)+1):
                if p[j-1] in ('.', s[i-1]):      dp[i][j]=dp[i-1][j-1]
                elif p[j-1]=='*':#dp[i][j-1]一次。 dp[i][j-2]   0次。   i-1对应*号。s:      aa   对应 p:  a*
                    dp[i][j]=dp[i][j-1] or dp[i][j-2] or (dp[i-1][j] and (p[j-2] in ('.', s[i-1]))    )
        return dp[-1][-1]  #背下上面这行就搞定了  #当j==1, ==*时候，因为dp[i-1][j]必须False。走不到p[j-2]
'''


'''
#可以通过的递归版本的另一种写法
class Solution:
    # @param s, an input string
    # @param p, a pattern string
    # @return a boolean
    def isMatch(self, s, p):
        if s and p and p[-1] not in (s[-1], '*', '.'): return False  #这一行是为了通过leetcode.  其实要删掉
        return self.dfs(s, p)

    def dfs(self, s, p):
        if not p: return not s
        if len(p)>=2 and p[1]=='*':
            i = 0
            while i< len(s) and  p[0] in ('.', s[i]):  #*号一下子match好多个数
                if self.dfs(s[i:], p[2:]): return True
                i+=1
            return self.dfs(s[i:], p[2:])    #最后为空得时候
        else: return s!='' and p[0] in ('.', s[0]) and self.dfs(s[1:], p[1:])
'''