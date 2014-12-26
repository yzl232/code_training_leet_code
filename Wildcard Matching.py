'''
Implement wildcard pattern matching with support for '?' and '*'.

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
isMatch("aa","a") → false
isMatch("aa","aa") → true
isMatch("aaa","aa") → false
isMatch("aa", "*") → true
isMatch("aa", "a*") → true
isMatch("ab", "?*") → true
isMatch("aab", "c*a*b") → false

'''
class Solution:
    # @param s, an input string
    # @param p, a pattern string
    # @return a boolean
    #http://blog.csdn.net/lifajun90/article/details/10582733
    #http://yucoding.blogspot.com/2013/02/leetcode-question-123-wildcard-matching.html
    def isMatch(self, s, p):
        m = len(s) ; n = len(p)
        j = i = match = 0; star = -1 #i==pPointer.  j==sPointer
        while i < m:
            if j < n and p[j] == '*':
                star = j; j +=1; match = i;
            elif j < n and (p[j] in ('?', s[i]) ):
                i+=1; j +=1
            elif star != -1:  # not match, 逐个增加*适配的范围。 看看结果
                j = star + 1; match+=1; i = match
            else:   return False
        while j < n and p[j] == '*':   j +=1
        return  j == n