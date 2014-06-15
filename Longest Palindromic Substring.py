class Solution: #DP
    # @return a string
    def longestPalindrome(self, s):  # http://blog.csdn.net/feliciafay/article/details/16984031
        n = len(s)
        begin = 0
        end = 0
        dp = [[False for i in range(n)] for j in range(n)]
        for i in range(n):
            dp[i][i] = True
        for i in range(n-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = True
                begin = i
                end = i+2
        for length in range(3, n+1):
            for i in range(0, n-length+1):
                j = i + length - 1
                if s[i] == s[j] and dp[i+1][j-1]:
                    dp[i][j] = True
                    begin = i
                    end = j+1
        return  s[begin:end]




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
