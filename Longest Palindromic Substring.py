'''
Given a string S, find the longest palindromic substring in S. You may assume that the maximum length of S is 1000, and there exists one unique longest palindromic substring.
'''

class Solution:  #优势在于space可以为O(1)
    # @return a string
    def expand(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1; r += 1
        return  (l+1, r-1, r-l-1)  #start, end length
    def longestPalindrome(self, s):
        ret =(0, 0, 1)
        for i in range(len(s)):
            r1 = self.expand(s, i, i)  #odd
            if r1[-1]>ret[-1]: ret = r1
            r2 = self.expand(s, i, i + 1)  #even
            if r2[-1]>ret[-1]: ret = r2
        return s[ret[0]:ret[1]+1]


'''
class Solution:
    # @return a string
    def longestPalindrome(self, s):
        if len(s)==0:  return 0
        ret=1
        start=0
        for i in range(len(s)):
            if i-ret >=1 and s[i-ret-1:i+1]==s[i-ret-1:i+1][::-1]:
                start=i-ret-1
                ret+=2
                continue
            if i-ret >=0 and s[i-ret:i+1]==s[i-ret:i+1][::-1]:
                start=i-ret
                ret+=1
        return s[start:start+ret]
and there are memory slicing tricks will help to bring these operations to O(1) time. comparing string equality with "==" is O(1), and using slicing to substring and reverse is also O(1)

'''



'''
class Solution:   # O(n) solution
    # @return a string
    def longestPalindrome(self, s):  # http://leetcode.com/2011/11/longest-palindromic-substring-part-ii.html
        T = self.process(s)
        C = 0  # central point
        R = 0  # the boundry point of the maximum palindrome.  C+P[C]
        P = [0 for i in range(len(T))]
        for i in range(1, len(T)-1):
            i_mirror = 2*C - i
            P[i] = min(R-i, P[i_mirror]) if R>i else 0     #min(R-i, 
            while T[i+1+P[i]] == T[i-1-P[i]]:  # // Attempt to expand palindrome centered at i
                P[i] = P[i] + 1
            #If palindrome centered at i expand past R,   adjust center based on expanded palindrome.
            if i+P[i] > R:
                C = i
                R = i + P[i]

        maxLen = 0
        centerIndex = 0
        for i in range(1, len(T) - 1):
            if P[i] > maxLen:
                maxLen = P[i]
                centerIndex = i
        startPoint = (centerIndex-maxLen-1)/2
        return s[startPoint: startPoint+maxLen]



    def process(self, s):
        ret = '^'
        for i in range(0, len(s)):
            ret += '#'+s[i]
        ret +='#$'
        return ret



dp解法

class Solution:
    # @return a string
    def longestPalindrome(self, s):  # http://blog.csdn.net/feliciafay/article/details/16984031
        n = len(s)
        start = 0
        end = 0
        dp = [[False for i in range(n)] for j in range(n)]
        maxL = -1
        for j in range(n):
            for i in range(j, -1, -1):
                if s[i] == s[j] and (j-i<=1 or dp[i+1][j-1]):
                    dp[i][j] = True
                    if j-i>maxL:
                        start = i
                        end = j+1
                        maxL = j-i
        return  s[start: end]#如出一辙 https://oj.leetcode.com/submissions/detail/13147843/
'''