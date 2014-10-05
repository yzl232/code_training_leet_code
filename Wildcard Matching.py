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
