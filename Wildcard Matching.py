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
        len_s = len(s) ; len_p = len(p)
        pPointer = sPointer = match = 0
        star = -1
        while sPointer < len_s:
            if pPointer < len_p and (p[pPointer] == '?' or p[pPointer] == s[sPointer] ):
                sPointer+=1; pPointer +=1
                continue
            if pPointer < len_p and p[pPointer] == '*':
                star = pPointer; pPointer +=1; match = sPointer;
                continue
            if star != -1:  # not match, 逐个增加*适配的范围。 看看结果
                pPointer = star + 1; match+=1; sPointer = match
                continue
            return False
        while pPointer < len_p and p[pPointer] == '*':
            pPointer +=1
        return  pPointer == len_p
